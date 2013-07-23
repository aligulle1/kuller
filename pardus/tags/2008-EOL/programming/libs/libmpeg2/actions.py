#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir="mpeg2dec-%s" % get.srcVERSION()

def setup():
    libtools.libtoolize()
    autotools.configure("--enable-shared \
                         --disable-static \
                         --disable-sdl \
                         --without-x")

def build():
    autotools.make('OPT_CFLAGS="%s" \
                    MPEG2DEC_CFLAGS="%s" \
                    LIBMPEG2_CFLAGS=""' % (get.CFLAGS(), get.CFLAGS()))

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
