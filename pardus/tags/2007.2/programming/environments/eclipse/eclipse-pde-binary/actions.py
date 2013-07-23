#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    pisitools.dodir("/opt")
    shelltools.copytree("eclipse", "%s/opt/eclipse" % get.installDIR())
    
    pisitools.remove("/opt/eclipse/notice.html")
    pisitools.remove("/opt/eclipse/epl-v10.html")
