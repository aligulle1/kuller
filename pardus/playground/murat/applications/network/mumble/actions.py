#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("qmake-qt4 main.pro \
                       QMAKE_CFLAGS+='%s' \
                       QMAKE_CXXFLAGS+='%s' \
                       QMAKE_CXX=%s \
                       QMAKE_CC=%s \
                       CONFIG+=no-bundled-speex \
                       CONFIG+=no-g15 \
                       CONFIG+=no-portaudio \
                       CONFIG+=no-oss \
                       CONFIG+=no-speechd \
                       CONFIG+=no-update \
                       CONFIG+=no-embed-qt-translation \
                       CONFIG+=no-ice \
                       DEFINIES+=NO_UPDATE_CHECK \
                       DEFINES+=PLUGIN_PATH=/usr/lib/mumble"
                       % (get.CFLAGS(), get.CXXFLAGS(), get.CXX(), get.CC()))

def build():
    autotools.make()

def install():
    pisitools.dobin("release/mumble")
    pisitools.dobin("scripts/mumble-overlay")
    pisitools.dosbin("release/murmurd")

    pisitools.insinto("/usr/lib/mumble", "release/*.so*")
    pisitools.doexe("release/plugins/liblink.so", "/usr/lib/mumble")

    pisitools.insinto("/usr/share/applications", "scripts/mumble.desktop")

    for size in ("16x16", "32x32", "48x48", "64x64"):
        pisitools.insinto("/usr/share/icons/hicolor/%s/apps" % size, "icons/mumble.%s.png" % size, "mumble.png")

    pisitools.doman("man/*")
    pisitools.dodoc("CHANGES", "LICENSE", "README*")
