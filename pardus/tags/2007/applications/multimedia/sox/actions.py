#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-ogg-vorbis \
                         --enable-mad \
                         --enable-lame \
                         --enable-oss-dsp \
                         --enable-alsa-dsp \
                         --enable-fast-ulaw \
                         --enable-fast-alaw")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("Changelog", "README", "TODO", "*.txt")
