#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "djvulibre-3.5.17"

def setup():
    pisitools.dosed("gui/nsdejavu/Makefile.in", "netscape", "nsbrowser")
    autotools.configure("--with-qt=/usr/qt/3 \
                         --enable-djview \
                         --enable-threads \
                         --enable-desktopfiles \
                         --enable-xmltools \
                         --enable-i18n \
                         --with-jpeg \
                         --with-tiff")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
