#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    kde.configure("--with-kde \
                   --sysconfdir=/usr/kde/3.5/share/config \
                   --with-pic \
                   --with-glut \
                   --enable-pch \
                   --enable-theora \
                   --without-arts \
                   --without-lua")

def build():
    kde.make()

def install():
    kde.install()

    pisitools.insinto("/usr/kde/3.5/share/celestia/","%s/usr/kde/3.5/share/apps/celestia/*" % get.installDIR())
    pisitools.removeDir("/usr/kde/3.5/share/apps/celestia")
    pisitools.dosym("/usr/kde/3.5/share/celestia","/usr/kde/3.5/share/apps/celestia")
