#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="ooo-build-%s" % get.srcVERSION()

def setup():
    shelltools.export("WANT_AUTOCONF","2.5")
    shelltools.export("CFLAGS", "%s -O2 -fno-strict-aliasing" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -O2 -fno-strict-aliasing" % get.CXXFLAGS())

    shelltools.system("./autogen.sh \
                       --prefix=/opt/OpenOffice.org \
                       --sysconfdir=/etc \
                       --with-lang=\"en-US de it nl tr\" \
                       --disable-post-install-scripts \
                       --with-installed-ooo-dirname=ooo-2.0 \
                       --enable-hunspell \
                       --disable-gtk \
                       --disable-cairo \
                       --disable-mono \
                       --with-distro=Pardus")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # We have our own desktop files
    pisitools.remove("/usr/share/applications/*")

    # Remove old links
    pisitools.remove("/opt/OpenOffice.org/bin/*")

    # New links
    apps = ["oobase", "oodraw", "oomath", "ooimpress", "oocalc", "oowriter"]
    for app in apps:
        pisitools.dosym("/opt/OpenOffice.org/bin/ooo-wrapper.py", "/usr/bin/%s" % app)

    # Icon symlinks
    pisitools.dosym("/usr/share/pixmaps/ooo-impress2.0.png","/usr/share/pixmaps/presentation.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-writer2.0.png","/usr/share/pixmaps/wordprocessing.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-calc2.0.png","/usr/share/pixmaps/spreadsheet.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-base2.0.png","/usr/share/pixmaps/database.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-draw2.0.png","/usr/share/pixmaps/drawing.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-math2.0.png","/usr/share/pixmaps/formula.png")

