#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "mozilla"

def setup():
    autotools.configure('--enable-optimize="%s -fno-strict-aliasing"' % get.CXXFLAGS())

def build():
    autotools.make()

    locales = ["be", "de", "es-AR", "es-ES", "fr", "it", "nl", "pt-PT" ,"tr"]

    for locale in locales:
        autotools.make("-C browser/locales libs-%s" % locale)
        pisitools.copy("dist/xpi-stage/locale-%s/chrome/%s.jar" % (locale, locale), "dist/bin/chrome/")
        pisitools.copy("dist/xpi-stage/locale-%s/chrome/%s.manifest" % (locale, locale), "dist/bin/chrome/")

def install():
    pisitools.insinto("/usr/lib/", "dist/bin", "MozillaFirefox", sym=False)

    pisitools.insinto("/usr/lib/MozillaFirefox", "dist/include/", "include", sym=False)
    pisitools.insinto("/usr/lib/MozillaFirefox", "dist/idl/", "idl", sym=False)

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
    pisitools.removeDir("/usr/lib/MozillaFirefox/chrome/icons")

    # Install docs
    pisitools.dodoc("LEGAL", "LICENSE")
