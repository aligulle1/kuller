#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("HOME", get.workDIR())
    autotools.configure("--with-nrpe-user=nrpe \
                         --with-nrpe-group=nrpe \
                         --with-nrpe-port=5666 \
                         --with-nagios-user=nagios \
                         --with-nagios-group=nagios \
                         --with-kerberos-inc=/usr/include \
                         --bindir=/usr/sbin \
                         --libexecdir=/usr/lib/nagios/plugins \
                         --localstatedir=/var/log/nagios \
                         --sysconfdir=/etc/nagios \
                         --enable-ssl \
                         --disable-static")

def build():
    autotools.make("all")
    shelltools.cd("contrib/")
    shelltools.system("gcc -o nrpe_check_control nrpe_check_control.c")

def install():
    autotools.make("DESTDIR=%s install-plugin install-daemon install-daemon-config" % get.installDIR())
    pisitools.insinto("/usr/lib/nagios/plugins", "contrib/nrpe_check_control")
    pisitools.dodir("/var/run/nrpe")
    pisitools.dodoc("LEGAL", "README", "README.SSL", "SECURITY", "docs/NRPE.odt", "docs/NRPE.pdf", "contrib/README.nrpe_check_control")
