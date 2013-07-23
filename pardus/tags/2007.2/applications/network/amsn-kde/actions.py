#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="desktop_integration"

def install():
    
    pisitools.dodir("/usr/share/amsn/plugins/amsn-kde")
    shelltools.copy("desktop_integration.tcl","%s/usr/share/amsn/plugins/amsn-kde/desktop_integration.tcl" % get.installDIR())
    shelltools.copy("plugininfo.xml","%s/usr/share/amsn/plugins/amsn-kde/plugininfo.xml" % get.installDIR())
