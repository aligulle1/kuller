#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "mozilla"

shelltools.export("MOZ_BUILD_DATE", "2007111515")
shelltools.export("BUILD_OFFICIAL", "1")
shelltools.export("MOZILLA_OFFICIAL", "1")

def setup():
    autotools.configure('--enable-optimize="%s -Os"' % get.CXXFLAGS())

def build():
    autotools.make()

    locales = ["be", "es-AR", "es-ES", "en-GB", "de", "fr", "it", "nl", "tr", "pt-BR"]

    for locale in locales:
        autotools.make("-C mail/locales libs-%s" % locale)
        pisitools.copy("dist/xpi-stage/locale-%s/chrome/%s.jar" % (locale, locale), "dist/bin/chrome/")
        pisitools.copy("dist/xpi-stage/locale-%s/chrome/%s.manifest" % (locale, locale), "dist/bin/chrome/")

def install():
    pisitools.insinto("/usr/lib/", "dist/bin", "MozillaThunderbird", sym=False)

    # Fake symlinks to get Turkish spell check support working
    pisitools.dosym("/usr/lib/MozillaThunderbird/dictionaries/en-US.aff","/usr/lib/MozillaThunderbird/dictionaries/tr-TR.aff")
    pisitools.dosym("/usr/lib/MozillaThunderbird/dictionaries/en-US.dic","/usr/lib/MozillaThunderbird/dictionaries/tr-TR.dic")

    # Install docs
    pisitools.dodoc("LEGAL", "LICENSE")
