#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--bindir=/bin \
                         --enable-largefile \
                         --enable-nls")

def build():
    autotools.make("LDFLAGS=%s" % get.LDFLAGS())
    autotools.make("RUN_VERY_EXPENSIVE_TESTS=yes check")
    autotools.make("check-root")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # move non-critical packages into /usr
    non_critical = ["csplit", "expand", "factor", "fmt", "fold", "join", \
                    "md5sum", "nl", "od", "paste", "pathchk", "pinky", \
                    "pr", "printf", "sha1sum", "shred", "sum", "tac", \
                    "tail", "test", "[", "tsort", "unexpand", "users"]

    for file in non_critical:
        pisitools.domove("/bin/%s" % file, "/usr/bin/", file)

    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "THANKS", "TODO")

    for file in shelltools.ls("%s/bin/" % get.installDIR()):
        pisitools.dosym("/bin/%s" % file, "/usr/bin/%s" % file)

    # This is installed by net-tools
    pisitools.remove("/bin/hostname")
    pisitools.remove("/usr/bin/hostname")
    pisitools.remove("/usr/share/man/man1/hostname.1")

    # These come from shadow package
    pisitools.remove("/usr/share/man/man1/login.1")
    pisitools.remove("/bin/su")
    pisitools.remove("/usr/bin/su")
    pisitools.remove("/usr/share/man/man8/lastlog.8")
    pisitools.remove("/usr/bin/lastlog")
    pisitools.remove("/usr/share/man/man5/faillog.5")
    pisitools.remove("/usr/bin/faillog")
    pisitools.remove("/usr/share/man/man8/faillog.8")
    pisitools.remove("/usr/share/man/man1/su.1")

    # These come from procps
    pisitools.remove("/usr/bin/uptime")
    pisitools.remove("/usr/share/man/man1/uptime.1")
