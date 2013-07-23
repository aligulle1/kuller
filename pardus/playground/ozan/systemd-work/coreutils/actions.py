#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


movetobin = ["arch", "basename", "cat", "chgrp", "chmod", "chown", "cp", "cut", "date", "dd", "df",
             "dir", "echo", "env", "false", "link", "ln", "ls", "mkdir", "mknod", "mktemp", "mv",
             "nice", "pwd", "readlink", "rm", "rmdir", "sleep", "sort", "stty", "sync", "touch",
             "true", "uname", "unlink", "vdir"]

symtousrbin = ["env", "cut", "readlink"]

def setup():
    shelltools.chmod("tests/misc/sort-mb-tests", 0755)
    shelltools.chmod("tests/df/direct", 0755)
    shelltools.export("AUTOPOINT", "true")
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing -fPIC -D_GNU_SOURCE=1" % get.CFLAGS())

    shelltools.export("AT_M4DIR", "m4")
    autotools.autoreconf("-vfi")

    # Fedora also installs su and hostname
    autotools.configure("--enable-largefile \
                         --enable-install-program=arch \
                         --enable-no-install-program=faillog,hostname,login,lastlog,uptime,kill \
                         DEFAULT_POSIX2_VERSION=200112")

    shelltools.touch("man/*.x")

def build():
    autotools.make("all LDFLAGS=%s" % get.LDFLAGS())
    pisitools.dosed("doc/coreutils.texi", "etc\/utmp", "var/run/utmp")
    pisitools.dosed("doc/coreutils.texi", "etc\/wtmp", "var/run/wtmp")

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #autotools.rawInstall("mandir=%s/%s install-man" % (get.installDIR(), get.manDIR()))

    # Use dircolors from the package
    pisitools.insinto("/etc", "src/dircolors.hin", "DIR_COLORS")

    # move critical files into /bin
    for f in movetobin:
        pisitools.domove("/usr/bin/%s" % f, "/bin/")

    for f in symtousrbin:
        pisitools.dosym("../../bin/%s" % f, "/usr/bin/%s" % f)

    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "THANKS", "TODO")

