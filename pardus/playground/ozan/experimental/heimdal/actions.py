#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    shelltools.export("AT_M4DIR", "cf")
    autotools.autoreconf("-fi")

    autotools.configure("--prefix=/opt/heimdal \
                         --libexecdir=/opt/heimdal/libexec \
                         --disable-osfc2 \
                         --disable-static \
                         --with-hdbdir=/var/lib/heimdal \
                         --with-x \
                         --with-ipv6 \
                         --with-readline \
                         --with-readline-lib=/lib \
                         --with-readline-include=/usr/include/readline \
                         --with-sqlite3=/usr \
                         --with-openldap=/usr \
                         --enable-shared \
                         --enable-pk-init \
                         --enable-kcm")


def build():
    autotools.make("-j1")

def install():
    shelltools.export("INSTALL_CATPAGES", "no")
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # Add "k" prefix to some apps and manpages to resolve conflicts
    """
    for app in ["telnetd", "ftpd", "popper", "rshd"]:
        pisitools.rename("/usr/share/man/man8/%s.8" % app, "k%s.8" % app)
        pisitools.rename("/usr/sbin/%s" % app, "k%s" % app)

    for app in ["rcp", "rsh", "su", "telnet", "ftp"]:
        pisitools.rename("/usr/share/man/man1/%s.1" % app, "k%s.1" % app)
        pisitools.rename("/usr/bin/%s" % app, "k%s" % app)

    pisitools.rename("/usr/bin/login", "login.heimdal")
    pisitools.rename("/usr/share/man/man1/login.1", "login.heimdal.1")
    """

    # From man-pages
    pisitools.remove("/usr/share/man/man5/ftpusers.5")

    pisitools.dodoc("README", "NEWS", "TODO", "ChangeLog")

    pisitools.dodir("/var/heimdal")
