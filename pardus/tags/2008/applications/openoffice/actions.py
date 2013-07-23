#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="ooo-build-%s" % get.srcVERSION()

def setup():
    shelltools.system('./configure \
                       --prefix=/opt/OpenOffice.org \
                       --sysconfdir=/etc \
                       --with-lang="en-US de es fr it nl pt-BR tr" \
                       --disable-post-install-scripts \
                       --disable-gtk \
                       --disable-cairo \
                       --disable-mono \
                       --with-distro=Pardus2008 \
                       --with-drink=nargile \
                       --with-num-cpus=2 \
                       --with-max-jobs=5')


def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove old links
    pisitools.remove("/opt/OpenOffice.org/bin/*")

    # New links
    apps = ["oobase", "oodraw", "oomath", "ooimpress", "oocalc", "oowriter"]
    for app in apps:
        pisitools.dosym("/opt/OpenOffice.org/bin/ooo-wrapper.py", "/usr/bin/%s" % app)

    # Icons
    pisitools.insinto("/usr/share/pixmaps","desktop/48x48/*.png")

    # Icon symlinks
    pisitools.dosym("/usr/share/pixmaps/ooo-impress.png","/usr/share/pixmaps/presentation.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-writer.png","/usr/share/pixmaps/wordprocessing.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-calc.png","/usr/share/pixmaps/spreadsheet.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-base.png","/usr/share/pixmaps/database.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-draw.png","/usr/share/pixmaps/drawing.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-math.png","/usr/share/pixmaps/formula.png")

    pisitools.dodoc("AUTHORS","ChangeLog","COPYING","NEWS","README")
