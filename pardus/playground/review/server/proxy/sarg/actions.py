#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--sysconfdir=/etc/sarg \
                         --mandir=/usr/share/man/man1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/sarg", "sarg-php")
    pisitools.chmod("%s/usr/share/sarg/images/*" %(get.installDIR()), 0644)
    pisitools.chmod("%s/etc/sarg/*" %(get.installDIR()), 0644)

    pisitools.removeDir("/usr/share/sarg/fonts")

    pisitools.dodoc("BETA-TESTERS", "ChangeLog", "CONTRIBUTORS", "COPYING", "DONATIONS", "LICENSE", "README")
    pisitools.dodoc("documentation/*")
