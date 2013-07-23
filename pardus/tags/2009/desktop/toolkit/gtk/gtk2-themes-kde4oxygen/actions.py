#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir = "."

def install():
    shelltools.copytree("kde4-oxygen", "%s/usr/share/themes/Oxygen" % get.installDIR())
    pisitools.removeDir("/usr/share/themes/Oxygen/metacity-1")

    #fix permissions of directories and files
    for dirpath, dirs, files in os.walk("%s/usr/share/themes/Oxygen" % get.installDIR()):
        shelltools.chmod(dirpath, 0755)
        for file in files:
            shelltools.chmod(os.path.join(dirpath, file), 0644)
