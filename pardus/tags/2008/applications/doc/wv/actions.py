#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-libwmf \
                         --with-libxml2 \
                         --with-docdir=/usr/share/doc/%s" % get.srcTAG())

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/include", "wvinternal.h")
    pisitools.remove("/usr/share/man/man1/wvConvert.1")
    pisitools.dosym("/usr/share/man/man1/wvWare.1", "/usr/share/man/man1/wvConvert.1")
