#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.aclocal()
    autotools.autoconf()
    autotools.automake()

    autotools.configure("--enable-bzlib2 \
                         --enable-zlib \
                         --enable-mysql \
                         --enable-postgresql \
                         --enable-sqlite \
                         --enable-net \
                         --enable-curl \
                         --enable-qt \
                         --enable-kde \
                         --enable-sdl \
                         --enable-libxml \
                         --enable-xslt \
                         --enable-vb \
                         --with-bzlib2-libraries=/lib")

def build():
    autotools.make()

def install():
    autotools.install("ROOT=%s" % get.installDIR())
    pisitools.dolib("src/exec/.libs/lib.gb.so.0.0.0", "/usr/lib/gambas")
    pisitools.dosym("lib.gb.so.0.0.0", "/usr/lib/gambas/lib.gb.so")
    pisitools.dosym("lib.gb.so.0.0.0", "/usr/lib/gambas/lib.gb.so.0")
    pisitools.insinto("/usr/lib/gambas", "src/exec/lib.gb.la")

    pisitools.insinto("/usr/share/icons/hicolor/16x16/apps", "app/gambas/img/logo/gambas-16x16.png", "gambas.png")
    pisitools.insinto("/usr/share/icons/hicolor/32x32/apps", "app/gambas/img/logo/gambas-32x32.png", "gambas.png")
    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps", "app/gambas/img/logo/gambas-48x48.png", "gambas.png")
    pisitools.insinto("/usr/share/icons/hicolor/64x64/apps", "app/gambas/img/logo/gambas-64x64.png", "gambas.png")

    pisitools.dodoc("AUTHORS", "COPYING*", "README*", "TODO", "ChangeLog*", "NEWS*")
