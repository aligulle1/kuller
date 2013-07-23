#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

WorkDir = "Io-2008-01-20"

def setup():
    # Remove unbuild addons
    for dirs in ["AppleExtras", "CFFI", "Contracts", "DBI", "GLFW", "HDB",
                 "ObjcBridge", "ODE", "QDBM", "SGML", "SkipDB", "SoundTouch", "TagDB"]:
        shelltools.unlinkDir("addons/%s" % dirs)

def build():
    autotools.make("INSTALL_PREFIX=/usr")

def install():
    autotools.install("INSTALL_PREFIX=%s/usr" % get.installDIR())

    # Upstream's makefile installs lots of unwanted parts of the addons, so we hack it
    pisitools.removeDir("/usr/lib/io/addons")
    for dirs in os.listdir("addons"):
        pisitools.insinto("/usr/lib/io/addons/%s/_build/dll" % dirs, "addons/%s/_build/dll/*" % dirs)
        pisitools.insinto("/usr/lib/io/addons/%s" % dirs, "addons/%s/build.io" % dirs)
        pisitools.insinto("/usr/lib/io/addons/%s" % dirs, "addons/%s/depends" % dirs)

    pisitools.insinto("/usr/share/doc/%s/Flux/SongJam" % get.srcTAG(), "addons/Flux/samples/SongJam/*.txt")
    pisitools.insinto("/usr/share/doc/%s/Flux/Diagram" % get.srcTAG(), "addons/Flux/samples/Diagram/notes/*.txt")
    pisitools.insinto("/usr/share/doc/%s/Flux/Slideshow" % get.srcTAG(), "addons/Flux/samples/Slideshow/*.txt")
    pisitools.insinto("/usr/share/doc/%s/Flux/resources" % get.srcTAG(), "addons/Flux/resources/themes/Milk/*.txt")
    pisitools.insinto("/usr/share/doc/%s/Flux/resources" % get.srcTAG(), "addons/Flux/resources/themes/Neos/*.txt")
    pisitools.insinto("/usr/share/doc/%s/OpenGL" % get.srcTAG(), "addons/OpenGL/samples/game/*.txt")
    pisitools.insinto("/usr/share/doc/%s/html/OpenGL" % get.srcTAG(), "addons/OpenGL/docs/*")
    pisitools.dohtml("docs/guide.html")
    pisitools.newdoc("libs/basekit/source/simd_cph/LICENSE.txt", "simd_cph_LICENSE.txt")
    pisitools.dodoc("libs/basekit/license/bsd_license.txt", "docs/guide.pdf")
