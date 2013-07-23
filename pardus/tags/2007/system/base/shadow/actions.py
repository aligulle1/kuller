#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    libtools.gnuconfig_update()
    libtools.libtoolize("--copy --force")

    shelltools.export("LDFLAGS", "%s -Wl,-z,now" % get.LDFLAGS())

    parameters = "--disable-desrpc \
                  --with-libcrypt \
                  --with-libcrack \
                  --enable-shared=no \
                  --enable-static=yes \
                  --with-libpam \
                  --without-libskey \
                  --without-selinux \
                  --enable-nls"

    autotools.configure(parameters)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.chmod(get.installDIR() + "/bin/su", 04711)

    for file in ["chfn", "chsh", "chage", "expiry", "newgrp", "passwd", "gpasswd"]:
        shelltools.chmod("%s/usr/bin/%s" % (get.installDIR(), file), 04711)

    for extension in ["a", "la"]:
        for file in ["libshadow"]:
            pisitools.remove("/lib/%s.%s" % (file, extension))

    pisitools.insinto("/etc/", "etc/login.access")
    shelltools.chmod("%s/etc/login.access" % get.installDIR(), 0600)

    pisitools.insinto("/etc/", "etc/limits")
    shelltools.chmod("%s/etc/limits" % get.installDIR(), 0644)

    pisitools.domove("/usr/bin/passwd", "/bin/")
    pisitools.dosym("/bin/passwd", "/usr/bin/passwd")

    pisitools.dodoc("doc/INSTALL", "doc/README", "doc/WISHLIST", "doc/HOWTO")

    # groups come from coreutils package
    pisitools.remove("/usr/share/man/man1/groups.1")
    pisitools.remove("/bin/groups")

    # Conflicts with man-pages
    pisitools.remove("/usr/share/man/man3/getspnam.3")
    pisitools.remove("/usr/share/man/man5/passwd.5")
