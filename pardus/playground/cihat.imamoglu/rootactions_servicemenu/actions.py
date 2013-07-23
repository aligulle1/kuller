#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#installDIR = get.workDIR() +"/"+ get.srcNAME() + "_" + get.srcVERSION()
#print("----",installDIR)
WorkDir = "rootactions_servicemenu_2.4.5"

def setup():
    pass

def build():
    pass

def install():
    #print("------%s/%s",% (get.workDIR(), WorkDir))
    pisitools.dodir("/usr/kde/4/share/kde4/services/ServiceMenus/")
    shelltools.copy("Root_Actions_2.4.5/dolphin-KDE4/10-rootactionsfolders.desktop", "%s/usr/kde/4/share/kde4/services/ServiceMenus/" % get.installDIR())
    shelltools.copy("Root_Actions_2.4.5/dolphin-KDE4/11-rootactionsfiles.desktop" ,"%s/usr/kde/4/share/kde4/services/ServiceMenus/" % get.installDIR())
    pisitools.dodir("/usr/bin/")
    shelltools.copy("Root_Actions_2.4.5/rootactions-servicemenu.pl", "%s/usr/bin/" % get.installDIR())
    shelltools.chmod("%s/usr/bin/" % get.installDIR(),0755)

 
