#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    shelltools.export("DO_NOT_COMPILE", "ksirc wifi lanbrowsing")

    autotools.make("-f Makefile.cvs")
    kde.configure("--with-slp \
                   --with-wifi \
                   --disable-sametime-plugin \
                   --without-xmms \
                   --without-external-libgadu")

def build():
    kde.make()

def install():
    kde.install()

    shelltools.chmod("%s/bin/reslisa" % get.kdeDIR(), 04755)
    pisitools.dodir("/etc")
    shelltools.touch("%s/etc/lisarc" % get.installDIR())

    # We replace this file
    pisitools.remove("/usr/kde/3.5/share/apps/konqueror/servicemenus/kget_download.desktop")
