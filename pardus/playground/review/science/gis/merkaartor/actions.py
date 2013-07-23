#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt4

def setup():
    shelltools.system('lrelease src/src.pro')
    # LIBPROXY=1 is not given, problem occurs while trying to find proxy.h
    qt4.configure(parameters = "GEOIMAGE=1 \
                                GPSDLIB=1 \
                                NODEBUG=1 \
                                RELEASE=1 \
                                GDAL=1 \
                                PROJ=1")

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.dodoc("AUTHORS", "CHANGELOG", "CREDITS", "HACKING", "LICENSE*", "TODO")
