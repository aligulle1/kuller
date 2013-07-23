#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()

    shelltools.export("CFLAGS","%s -fsigned-char" % get.CFLAGS())

    autotools.configure("--disable-static \
                         --enable-ogg-vorbis \
                         --enable-mad \
                         --enable-lame \
                         --enable-gsm \
                         --enable-oss-dsp \
                         --enable-alsa-dsp \
                         --enable-fast-ulaw \
                         --enable-fast-alaw \
                         --with-samplerate \
                         --with-flac \
                         --with-sndfile \
                         --enable-largefile")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("Changelog", "README", "TODO", "*.txt")
