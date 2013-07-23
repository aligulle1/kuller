#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "thunderbird-3.0b2"

def setup():
    shelltools.makedirs("objdir")
    shelltools.cd("objdir")
    shelltools.system("../configure --prefix=/usr --libdir=/usr/lib")

def build():
    shelltools.cd("objdir")
    autotools.make("-j1")

def install():
    shelltools.cd("objdir")
    pisitools.insinto("/usr/lib/", "mozilla/dist/bin", "MozillaThunderbird", sym=False)

    # Fake symlinks to get Turkish spell check support working
    pisitools.dosym("/usr/lib/MozillaThunderbird/dictionaries/en-US.aff","/usr/lib/MozillaThunderbird/dictionaries/tr-TR.aff")
    pisitools.dosym("/usr/lib/MozillaThunderbird/dictionaries/en-US.dic","/usr/lib/MozillaThunderbird/dictionaries/tr-TR.dic")

    shelltools.cd("..")

    # Install icon
    pisitools.insinto("/usr/share/pixmaps", "other-licenses/branding/thunderbird/mailicon256.png", "thunderbird.png")

    # Install docs
    pisitools.dodoc("mozilla/LEGAL", "mozilla/LICENSE")
