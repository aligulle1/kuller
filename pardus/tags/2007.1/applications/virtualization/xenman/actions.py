#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/xenman/", "pixmaps")
    pisitools.insinto("/usr/share/xenman/", "src")
    pisitools.insinto("/usr/share/xenman/", "xenman.glade")

    pisitools.dodir("/var/cache/xenman/image_store")

    pisitools.chmod("/usr/share/xenman/src/xenman.py")

    pisitools.dosym("/usr/share/xenman/src/xenman.py", "/usr/bin/xenman")

    pisitools.dodoc("doc/changelog.txt", "doc/Image_Builders_Guide.txt", "doc/manual.html", "README")
