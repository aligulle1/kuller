#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr/nagios \
                            --localstatedir=/var/nagios \
                            --sysconfdir=/etc/nagios \
                            --datadir=/usr/nagios/share \
                            --mandir=/usr/share/man \
                            --infodir=/usr/share/info \
                            --enable-embedded-perl \
                            --with-perlcache \
                            --with-command-group=apache")

def build():
    autotools.make("CC=%s nagios" % get.CC())
    autotools.make("CC=%s DESTDIR=%s cgis" % (get.CC(),get.installDIR()))
    autotools.make("-C contrib all")

def install():
    autotools.make("DESTDIR=%s install" % get.installDIR())
    autotools.make("DESTDIR=%s install-config" % get.installDIR())
    autotools.make("DESTDIR=%s install-commandmode" % get.installDIR())
    pisitools.dodoc("Changelog", "LEGAL", "LICENSE", "THANKS", "README")
