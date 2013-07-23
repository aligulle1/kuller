#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.cd("src")
    autotools.rawConfigure("--enable-alsa \
                            --enable-jack")

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    pisitools.dobin("src/mixxx")
    pisitools.insinto("/usr/share/mixxx", "src/skins")
    pisitools.insinto("usr/share/mixxx", "src/keyboard")
    pisitools.insinto("usr/share/mixxx", "src/images")
    pisitools.insinto("usr/share/mixxx", "src/midi")
    pisitools.dodoc("README", "README.ALSA", "Mixxx-Manual.pdf")
