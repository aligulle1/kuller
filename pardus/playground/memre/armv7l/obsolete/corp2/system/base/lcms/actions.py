#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cache = [ "ac_cv_file__usr_include_python2_6_Python_h=yes", ]

    #needed by mozilla patch
    crosstools.autoreconf("-fi")
    crosstools.configure("--disable-dependency-tracking \
                          --disable-static \
                          --with-jpeg \
                          --with-tiff \
                          --with-zlib \
                          --with-python", cache=cache )

def build():
    #needed by mozilla patch, swig must be run again
    shelltools.cd("python")
    shelltools.system("./swig_lcms")
    shelltools.cd("..")

    crosstools.make()

def install():
    crosstools.rawInstall('DESTDIR=%s \
                           BINDIR=%s/usr/bin \
                           includedir=/usr/include \
                           program_transform_name=' % (get.installDIR(), get.installDIR()))

    pisitools.insinto("/usr/share/lcms/profiles", "testbed/*.icm")

    pisitools.dodoc("AUTHORS", "README*", "NEWS", "doc/*")
