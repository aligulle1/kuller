#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os
from os.path import join

WorkDir = "glest_game"

def setup():
    shelltools.cd("../")
    for root, dirs, files in os.walk(WorkDir):
        for name in dirs:
            shelltools.chmod(join(root, name), 0755)
        for name in files:
            shelltools.chmod(join(root, name), 0644)

def install():
    pisitools.dodir("/usr/share")
    shelltools.cd("../")
    shelltools.copytree(WorkDir, "%s/usr/share/glest" % get.installDIR())

    # Buggy character coding
    pisitools.remove("/usr/share/glest/data/lang/espa*")
    
    # We will use the ini file from the source code
    pisitools.remove("/usr/share/glest/glest.ini")
