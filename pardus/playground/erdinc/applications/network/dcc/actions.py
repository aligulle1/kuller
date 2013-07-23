#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", get.LDFLAGS() + "-Wl,-z,now")
    autotools.rawConfigure("--homedir=/etc/dcc \
                            --libexecdir=/usr/sbin \
                            --bindir=/usr/sbin \
                            --with-cgibin=%s/var/www/localhost/cgi-bin/dcc \
                            --disable-perl \
                            --disable-dccm \
                            --with-rundir=/var/run/dcc \
                            --enable-ipv6" % get.installDIR())

def build():
    autotools.make()

def install():
    shelltools.export("DCC_PROTO_HOMEDIR", "/etc/dcc")
    autotools.rawInstall("DESTDIR=%s DCC_BINDIR=%s/usr/sbin DCC_LIBEXEC=%s/usr/sbin \
                          BINDIR=%s/usr/bin DCC_CGIBINDIR=%s/var/www/localhost/cgi-bin/dcc \
                          MANDIR=%s/usr/share/man/man DCC_HOMEDIR=%s/etc/dcc" % (get.installDIR(), get.installDIR(), \
                          get.installDIR(), get.installDIR(), get.installDIR(), get.installDIR(), get.installDIR()))
    pisitools.dodoc("CHANGES")
    pisitools.domove("/usr/bin/dbclean", "/usr/sbin")
    pisitools.domove("/usr/bin/dblist", "/usr/sbin")
    pisitools.domove("/usr/bin/dccd", "/usr/sbin")
    pisitools.domove("/usr/bin/dccif-test", "/usr/sbin")
    pisitools.domove("/usr/bin/dccifd", "/usr/sbin")
    pisitools.domove("/usr/bin/dccsight", "/usr/sbin")
    pisitools.domove("/usr/bin/dns-helper", "/usr/sbin")
    pisitools.domove("/usr/bin/wlist", "/usr/sbin")
    pisitools.remove("/usr/sbin/updatedcc")
    pisitools.remove("/usr/sbin/uninstalldcc")
