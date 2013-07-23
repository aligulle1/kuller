#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def install():
    if shelltools.can_access_directory("/usr/kde/3.5/share/apps/dolphin/servicemenus/"):
        pisitools.insinto("/usr/kde/3.5/share/apps/dolphin/servicemenus/",""+get.workDIR()+"/dolphin-KDE3/*.desktop")


    if shelltools.can_access_directory("/usr/kde/3.5/share/apps/konqueror/servicemenus/"):
        pisitools.insinto("/usr/kde/3.5/share/apps/konqueror/servicemenus/",""+get.workDIR()+"/konqueror-KDE3/*.desktop")


    if shelltools.can_access_directory("/usr/kde/4/share/apps/krusader/"):
        pisitools.insinto("/usr/kde/4/share/apps/krusader/",""+get.workDIR()+"/krusader-KDE4/*.xml")


    if shelltools.can_access_directory("/usr/kde/4/share/kde4/services/ServiceMenus/"):
        pisitools.insinto("/usr/kde/4/share/kde4/services/ServiceMenus/",""+get.workDIR()+"/dolphin-konqueror-KDE4/*.desktop")

    pisitools.dobin("rootactions-servicemenu.pl")
    pisitools.dodoc("README","changelog","GPL-2")