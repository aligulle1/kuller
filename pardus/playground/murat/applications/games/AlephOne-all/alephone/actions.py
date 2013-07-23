#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "AlephOne-%s" % get.srcVERSION().split("_")[1]

def setup():
    autotools.configure("--enable-opengl \
                         --enable-mad \
                         --enable-sndfile \
                         --enable-vorbis \
                         --enable-lua \
                         --disable-sdltest")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README")
