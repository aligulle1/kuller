#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "droid-%s" % get.srcVERSION().split("_", 1)[1]

def install():
    shelltools.chmod("*.ttf",0644)

    pisitools.insinto("/usr/share/fonts/droid","*.ttf")

    pisitools.dosym("../conf.avail/69-droid-fonts-sans-fontconfig.conf", "/etc/fonts/conf.d/69-droid-fonts-sans-fontconfig.conf")
    pisitools.dosym("../conf.avail/70-droid-fonts-sans-mono-fontconfig.conf", "/etc/fonts/conf.d/70-droid-fonts-sans-mono-fontconfig.conf")
    pisitools.dosym("../conf.avail/71-droid-fonts-serif-fontconfig.conf", "/etc/fonts/conf.d/71-droid-fonts-serif-fontconfig.conf")
