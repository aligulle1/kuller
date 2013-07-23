#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-gtktest \
                         --disable-sdltest \
                         --with-mp3 \
                         --with-jpeg \
                         --with-vorbis \
                         --enable-gtk2 \
                         --disable-lua-binaries")

def build():
    autotools.make()

def install():
    pisitools.dobin("src/stepmania")
    pisitools.doexe("src/GtkModule.so", "/usr/lib/StepMania")

    pisitools.dodoc("Docs/*")
