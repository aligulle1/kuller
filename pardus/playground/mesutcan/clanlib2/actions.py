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
    autotools.autoreconf("-vfi")

    autotools.configure("--enable-gl \
                         --enable-clanDisplay \
                         --enable-clanGL \
                         --enable-clanGL1 \
                         --enable-clanSound \
                         --enable-clanDatabase \
                         --enable-clanSqlite \
                         --enable-clanRegExp \
                         --enable-clanNetwork \
                         --enable-clanGUI \
                         --enable-clanGDI \
                         --enable-clanMikMod \
                         --enable-clanVorbis \
                         --enable-DirectFB \
                         --enable-x11 \
                         --enable-vorbis \
                         --enable-mikmod \
                         --enable-debug \
                         --enable-shared \
                         --enable-static \
                         --enable-docs")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

