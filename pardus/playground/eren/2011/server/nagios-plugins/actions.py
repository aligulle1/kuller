#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --libexecdir=/usr/lib/nagios/plugins \
                            --sysconfdir=/etc/nagios \
                            --disable-static \
                            --disable-libtap \
                            --with-ipv6 \
                            --with-smbclient-command=/usr/bin/smbclient \
                            --with-openssl=/usr \
                            --with-pgsql=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
