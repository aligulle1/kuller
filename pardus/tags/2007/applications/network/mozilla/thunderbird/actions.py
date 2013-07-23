#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "mozilla"

def setup():
    shelltools.export("MOZ_CO_PROJECT", "mail")
    shelltools.export("BUILD_OFFICIAL", "1")
    shelltools.export("MOZILLA_OFFICIAL", "1")

    shelltools.export("WANT_AUTOCONF", "2.1")
    autotools.autoconf()
    autotools.configure()

def build():
    autotools.make()

    locales = ["ca", "cs", "da", "de", "el", "en-GB", "es-AR", \
               "es-ES", "eu", "fi", "fr", "ga-IE", "he", "hu", "it", \
               "ja", "ko", "lt", "mk", "nb-NO", "nl", "pl", "pt-BR",  \
               "ru", "sk", "sl", "sv-SE", "tr", "zh-CN"]

    for locale in locales:
        autotools.make("-C mail/locales libs-%s" % locale)
        pisitools.copy("dist/xpi-stage/locale-%s/chrome/%s.jar" % (locale, locale), "dist/bin/chrome/")
        pisitools.copy("dist/xpi-stage/locale-%s/chrome/%s.manifest" % (locale, locale), "dist/bin/chrome/")

def install():
    pisitools.insinto("/usr/lib/", "dist/bin", "MozillaThunderbird", sym=False)

    # Thunderbird is piece of crap, you need myspell en-US files in every
    # locale else this piece of shit won't work
    pisitools.dodir("/usr/lib/MozillaThunderbird/components/myspell")
    shelltools.copy("extensions/spellcheck/locales/en-US/myspell/en-US.*", "%s/usr/lib/MozillaThunderbird/components/myspell" % get.installDIR())

    # Install docs
    pisitools.dodoc("LEGAL", "LICENSE")
