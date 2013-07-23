#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    pisitools.dosed("metadata.desktop", "contents\/icon\.svgz", "lkd-uye")
    applet_name = "lkd-uye"
    pisitools.insinto("/usr/kde/4/share/apps/plasma/plasmoids", "contents", "%s/contents" % applet_name)
    pisitools.insinto("/usr/kde/4/share/apps/plasma/plasmoids/%s" % applet_name, "metadata.desktop")
    pisitools.insinto("/usr/kde/4/share/kde4/services", "metadata.desktop", "plasma-applet-%s.desktop" % applet_name)
    pisitools.dosym("contents/icon.svgz", "/usr/kde/4/share/apps/desktoptheme/default/widgets/lkd-uye.svgz")

