#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.automake()
    autotools.autoconf()

    autotools.configure("--disable-mp3x \
                         --disable-static \
                         --enable-shared \
                         --enable-mp3rtp \
                         --enable-nasm")

def build():
    # paralel derlenme problemleri var
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=\"%s\" pkghtmldir=\"/usr/share/doc/%s/html\"" % (get.installDIR(), get.srcTAG()))

    pisitools.dodoc("API", "ChangeLog", "HACKING", "PRESETS.draft", "README", "STYLEGUIDE", "TODO", "USAGE")
    pisitools.dohtml("misc/*", "Dll/*")
    pisitools.dobin("misc/mlame")
