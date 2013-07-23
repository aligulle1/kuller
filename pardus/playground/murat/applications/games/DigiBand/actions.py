#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir = "DigiBand"

datadir = "/usr/share/DigiBand"
NoStrip = datadir

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def build():
    shelltools.cd("Source")

    autotools.make("-f Makefile.linux \
                    DATADIR=%s" % datadir)

def install():
    pisitools.dodir(datadir)

    pisitools.dobin("Source/DigiBand")
    #pisitools.rename("/usr/bin/DigiBand", "DigiBand.bin")

    for data in ["Data", "Noteskins", "Songs", "Themes"]:
        fixperms(data)
        shelltools.copytree(data, "%s/%s" % (get.installDIR(), datadir))

    pisitools.dohtml("Documentation/*.html", "Documentation/*.jpg", "Documentation/*.gif")
    pisitools.dodoc("GPL.rtf", "*.txt", "Documentation/*.txt")
