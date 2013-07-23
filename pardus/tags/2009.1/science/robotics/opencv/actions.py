#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():

    autotools.autoreconf("-fi")

    # Python binding will be generated with SWIG then compiled
    # xine codecs will be used instead of quicktime or ffmpeg
    # (note: ffmpeg fails for some reason)
    # GUI will be gtk
    # Firewire and Video4Linux support will be compiled in
    # 1394libs is off because the new dc1394 lib broke ABI and this version
    # of opencv doesn't even detect it.
    autotools.configure("--with-swig \
                         --with-python \
                         --with-xine \
                         --with-ffmpeg \
                         --enable-jasper \
                         --enable-openexr \
                         --enable-tiff \
                         --enable-png \
                         --enable-zlib \
                         --enable-jpeg \
                         --without-quicktime \
                         --without-carbon \
                         --without-1394libs \
                         --with-gtk \
                         --with-v4l \
                         --with-v4l2")

    # Underlinking problems
    pisitools.dosed("otherlibs/highgui/Makefile", "^LIBS = (.*)$", "LIBS = \\1 -lavutil")
    pisitools.dosed("Makefile", "^LIBS = (.*)$", "LIBS = \\1 -lutil")


def check():
    autotools.make("check")

def build():
    autotools.make()

def install():
    autotools.install()

    # Move other docs and samples under standart doc dir
    doc_dir = "usr/share/doc/" + get.srcNAME()
    pisitools.domove("usr/share/opencv/doc", doc_dir)
    pisitools.domove("usr/share/opencv/samples", doc_dir)

    pisitools.dodoc("ChangeLog", "COPYING", "THANKS", "TODO")
