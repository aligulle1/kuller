#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("DO_NOT_COMPILE", "mpeglib mpeglib_artsplug kaboodle noatun")

    autotools.make("-f Makefile.cvs")
    kde.configure("--with-extra-includes=/usr/include/speex \
                   --with-akode \
                   --with-cdparanoia \
                   --enable-cdparanoia \
                   --with-arts-alsa \
                   --with-alsa \
                   --with-vorbis \
                   --with-lame \
                   --with-flac \
                   --with-speex \
                   --with-libmad \
                   --without-jack \
                   --with-xine \
                   --with-musicbrainz")

def build():
    kde.make()

def install():
    kde.install()
