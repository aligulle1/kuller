#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "portaudio_v18_1"

def build():
    autotools.make('CC="%s" AR="%s" RANLIB="%s" LD="%s" CFLAGS="%s"' %
                  (get.CC(), get.AR(), get.RANLIB(), get.LD(), get.CFLAGS()))

def install():
    autotools.rawInstall('DESTDIR="%s" libdir=/usr/lib' % get.installDIR())
    pisitools.dodoc("docs/*")
