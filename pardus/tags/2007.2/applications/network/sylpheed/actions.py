#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("sylpheed.desktop", "sylpheed.png", "sylpheed-128x128.png")
    autotools.configure("--enable-ldap \
                         --enable-compface \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/pixmaps")
    pisitools.insinto("/usr/share/pixmaps", "*.png")

    pisitools.insinto("/usr/share/applications", "sylpheed.desktop")
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS*", "README*", "TODO*")

