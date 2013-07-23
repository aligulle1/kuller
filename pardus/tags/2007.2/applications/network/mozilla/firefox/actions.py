#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "mozilla"

shelltools.export("MOZ_BUILD_DATE", "2007052900")
shelltools.export("BUILD_OFFICIAL", "1")
shelltools.export("MOZILLA_OFFICIAL", "1")

def setup():
    shelltools.export("WANT_AUTOCONF", "2.1")
    autotools.autoconf()

    # Mozilla has different approach for build itself
    # See http://www.mozilla.org/build/configure-build.html and mozconfig.patch
    autotools.configure('--enable-optimize="%s -Os"' % get.CXXFLAGS())

def build():
    autotools.make()

    locales = ["be", "es-AR", "es-ES", "en-GB", "de", "fr", "it", "nl", "tr", "pt-BR"]

    for locale in locales:
        autotools.make("-C browser/locales libs-%s" % locale)
        pisitools.copy("dist/xpi-stage/locale-%s/chrome/%s.jar" % (locale, locale), "dist/bin/chrome/")
        pisitools.copy("dist/xpi-stage/locale-%s/chrome/%s.manifest" % (locale, locale), "dist/bin/chrome/")

def install():
    pisitools.insinto("/usr/lib/", "dist/bin", "MozillaFirefox", sym=False)

    pisitools.insinto("/usr/lib/MozillaFirefox", "dist/include/", "include", sym=False)
    pisitools.insinto("/usr/lib/MozillaFirefox", "dist/idl/", "idl", sym=False)

    # Ldap headers
    pisitools.insinto("/usr/lib/MozillaFirefox/include", "dist/public/ldap/", "ldap", sym=False)
    pisitools.insinto("/usr/lib/MozillaFirefox/include", "dist/public/ldap-private", "ldap-private", sym=False)

    # Dirty hack to get some applications using this header running
    pisitools.dosym("/usr/lib/MozillaFirefox/include/necko/nsIURI.h", \
                    "/usr/lib/MozillaFirefox/include/nsIURI.h")

    # Remove bookmarks
    pisitools.remove("/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")

    # Firefox is piece of crap too
    pisitools.dodir("/usr/lib/MozillaFirefox/dictionaries")
    shelltools.touch("%s/usr/lib/MozillaFirefox/dictionaries/tr-TR.aff" % get.installDIR())
    shelltools.touch("%s/usr/lib/MozillaFirefox/dictionaries/tr-TR.dic" % get.installDIR())

    # Remove these
    pisitools.remove("/usr/lib/MozillaFirefox/defaults/profile/mimeTypes.rdf")
    pisitools.remove("/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
    pisitools.remove("/usr/lib/MozillaFirefox/.autoreg")

    # Install docs
    pisitools.dodoc("LEGAL", "LICENSE")
