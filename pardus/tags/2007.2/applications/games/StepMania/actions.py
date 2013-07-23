#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-gtktest \
                         --disable-sdltest \
                         --with-mp3 \
                         --with-jpeg \
                         --with-vorbis \
                         --enable-gtk2 \
                         --enable-force-oss ")

def build():
    autotools.make()

def install():
    pisitools.dobin("src/stepmania")
    pisitools.doexe("src/GtkModule.so", "/usr/lib/StepMania")

    pisitools.dodoc("Docs/*")
