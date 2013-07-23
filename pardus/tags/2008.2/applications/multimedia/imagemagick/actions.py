#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

WorkDir = "ImageMagick-%s" % get.srcVERSION()[:-3]

def setup():
    pisitools.dosed("configure","DOCUMENTATION_RELATIVE_PATH=.*","DOCUMENTATION_RELATIVE_PATH=%s/html" % get.srcTAG())
    autotools.configure("--with-gs-font-dir=/usr/share/fonts/default/ghostscript \
                         --enable-hdri \
                         --enable-shared \
                         --disable-static \
                         --enable-lzw \
                         --without-hdf \
                         --with-threads \
                         --with-djvu \
                         --with-bzlib \
                         --with-modules \
                         --with-zlib \
                         --with-x \
                         --with-wmf \
                         --with-fpx \
                         --with-perl \
                         --without-jbig \
                         --with-tiff \
                         --with-lcms \
                         --with-xml \
                         --with-jp2 \
                         --with-jpeg \
                         --with-mpeg2 \
                         --with-gslib \
                         --with-dot \
                         --with-ttf")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib/libltdl*")
    perlmodules.fixLocalPod()

    pisitools.dodoc("AUTHORS","ChangeLog","LICENSE","NEWS")
