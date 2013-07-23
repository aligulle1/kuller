# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    import zipfile

    jarname = "%s%s.jar" % (get.srcNAME(), get.srcVERSION())
    zipfile.ZipFile(jarname).extractall()
    pisitools.insinto("/usr/share/pixmaps", "com/neuemusic/eartoner/images/et_ico_64.png", "%s.png" % get.srcNAME())
    pisitools.insinto("/usr/share/%s" % get.srcNAME(), jarname, "%s.jar" % get.srcNAME())

