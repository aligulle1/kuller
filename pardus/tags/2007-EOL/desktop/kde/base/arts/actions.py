#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "arts-1.5.9"

def setup():
    kde.configure("--enable-alsa \
                   --enable-vorbis \
                   --enable-libmad \
                   --with-audiofile \
                   --without-nas \
                   --without-jack \
                   --without-esd \
                   --without-mas")

def build():
    kde.make()

def install():
    kde.install()

    # suid aRts, possible fix of http://bugs.pardus.org.tr/show_bug.cgi?id=262
    shelltools.chmod("%s/%s/bin/artswrapper" % (get.installDIR(), get.kdeDIR()), 04755)
