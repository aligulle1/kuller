#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-google \
                         --enable-terraserver \
                         --enable-expedia \
                         --enable-openstreetmap \
                         --enable-bluemarble \
                         --enable-geonames \
                         --enable-geocaches \
                         --enable-spotmaps \
                         --disable-dem24k")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.removeDir("/usr/share/man")
    pisitools.dodoc("COPYING","INSTALL","README","AUTHORS","ChangeLog","doc/*.*","doc/dev/*","doc/examples/*.*")