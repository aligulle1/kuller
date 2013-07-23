#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -I/usr/include/X11/fonts" % get.CFLAGS())
    autotools.autoreconf()

    autotools.configure("--with-x \
                         --enable-xfree-ext \
                         --enable-xvideo \
                         --enable-dv \
                         --enable-mmx \
                         --disable-motif \
                         --disable-quicktime \
                         --enable-alsa \
                         --enable-lirc \
                         --enable-gl \
                         --enable-zvbi \
                         --prefix=/usr \
                         --enable-aa")

def build():
    autotools.make()

def install():
    autotools.install("libdir=%(D)s/usr/lib/xawtv \
                       resdir=%(D)s/etc/X11" % {"D": get.installDIR()})

    pisitools.dodoc("COPYING", "Changes", "README*", "TODO")

    pisitools.removeDir("/usr/share/man/fr")
    pisitools.removeDir("/usr/share/man/es")

    pisitools.dodir("/usr/share/xawtv")
    pisitools.domove("/usr/share/*.list", "/usr/share/xawtv/")
    pisitools.domove("/usr/share/Index*", "/usr/share/xawtv/")
