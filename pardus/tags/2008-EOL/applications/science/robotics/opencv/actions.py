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
    # Python binding will be generated with SWIG then compiled
    # xine codecs will be used instead of quicktime or ffmpeg
    # (note: ffmpeg fails for some reason)
    # GUI will be gtk
    # Firewire and Video4Linux support will be compiled in
    autotools.configure("--with-swig \
                         --with-python \
                         --with-xine \
                         --without-ffmpeg \
                         --without-quicktime \
                         --without-carbon \
                         --with-gtk \
                         --with-1394libs \
                         --with-v4l")

def check():
    autotools.make("check")

def build():
    autotools.make()

def install():
    autotools.install()

    pythonmodules.fixCompiledPy()

    pisitools.dodoc("ChangeLog", "COPYING", "THANKS", "TODO")
    # Move other docs and samples under standart doc dir
    doc_dir = "usr/share/doc/" + get.srcTAG()
    pisitools.domove("usr/share/opencv/doc", doc_dir)
    pisitools.domove("usr/share/opencv/samples", doc_dir)
