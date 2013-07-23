#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="snack%s/unix" % get.srcVERSION()

def setup():
    autotools.rawConfigure("--with-tcl=/usr/lib \
                            --with-tk=/usr/lib \
                            --enable-alsa \
                            --enable-threads \
                            --with-ogg-include=/usr/include \
                            --with-ogg-lib=/usr/lib")

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/snack","*.so")
    pisitools.insinto("/usr/lib/snack","*.tcl")

    pisitools.dodoc("../doc/*.txt")
    pisitools.dohtml("../doc/*.html")
