#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir   = "comm-release"
MOZAPPDIR = "/usr/lib/MozillaThunderbird"

def build():
#    shelltools.export("LDFLAGS", "%s -Wl,-rpath,/usr/lib/thunderbird" % get.LDFLAGS())
    shelltools.export("LDFLAGS", "%s -Wl,-rpath,/usr/lib/MozillaThunderbird" % (get.LDFLAGS()))

    # Build thunderbird
    autotools.make("-f client.mk build")

    # Prepare language packs
    autotools.make("-f client.mk configure")

def install():
    autotools.make("-f client.mk DESTDIR='%s' install" % get.installDIR())

    pisitools.insinto("/usr/lib/", "mozilla/dist/bin", "MozillaThunderbird", sym=False)

    # Install default-prefs.js
    pisitools.insinto("%s/defaults/pref" % MOZAPPDIR, ".pardus-default-prefs.js", "all-pardus.js")

    # Empty fake files to get Turkish spell check support working
    pisitools.dodir("%s/extensions/langpack-tr@thunderbird.mozilla.org/dictionaries" % MOZAPPDIR)
    shelltools.touch("%s/%s/%s/dictionaries/tr-TR.aff" % (get.installDIR(), MOZAPPDIR, "extensions/langpack-tr@thunderbird.mozilla.org"))
    shelltools.touch("%s/%s/%s/dictionaries/tr-TR.dic" % (get.installDIR(), MOZAPPDIR, "extensions/langpack-tr@thunderbird.mozilla.org"))

    pisitools.removeDir("%s/dictionaries" % MOZAPPDIR)
    pisitools.dosym("/usr/share/hunspell", "%s/dictionaries" % MOZAPPDIR)


    # Remove this to avoid spellchecking dictionary detection problems
    pisitools.remove("/usr/lib/MozillaThunderbird/defaults/pref/all-l10n.js")

    # Install icons
    pisitools.insinto("/usr/share/pixmaps", "other-licenses/branding/thunderbird/mailicon256.png", "thunderbird.png")
    pisitools.insinto("%s/icons" % MOZAPPDIR, "other-licenses/branding/thunderbird/mailicon16.png")

    for s in (16, 22, 24, 32, 48, 256):
        pisitools.insinto("/usr/share/icons/hicolor/%dx%d/apps" % (s,s), "other-licenses/branding/thunderbird/mailicon%d.png" % s, "thunderbird.png")

    # Install docs
    pisitools.dodoc("mozilla/LEGAL", "mozilla/LICENSE")

    # We have our own wrapper
    pisitools.remove("/usr/bin/thunderbird")

    # Remove development stuff
    pisitools.removeDir("/usr/share/idl")
    pisitools.removeDir("/usr/include")
    pisitools.removeDir("/usr/lib/thunderbird-devel")

    # Remove useless file
    pisitools.remove("/usr/lib/MozillaThunderbird/.purgecaches")
