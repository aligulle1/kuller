#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "xorg-emgd-1.8.0.2032+pvr1.5.15.3226"
NoStrip = "/"

def install():
    pisitools.insinto("/etc", "etc/powervr.ini")

    pisitools.dolib("dri/*", "/usr/lib/dri")
    pisitools.dosym("/usr/lib/dri/emgd_dri.so", "/usr/lib/xorg/modules/dri/emgd_dri.so")
    pisitools.dosym("/usr/lib/dri/emgd_drv_video.so", "/usr/lib/xorg/modules/dri/emgd_drv_video.so")
    pisitools.dolib("drivers/emgd_drv.so", "/usr/lib/xorg/modules/drivers")
    pisitools.dolib("lib/*")

    pisitools.doman("man/emgd.4.gz")

    pisitools.dodoc("debian/changelog", "debian/copyright")
