#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

NoStrip = "/"

data = ["Announcers", "BackgroundEffects", "BackgroundTransitions",
        "BGAnimations", "CDTitles", "Characters", "Courses", "Data",
        "NoteSkins", "Packages", "RandomMovies", "Songs", "Themes"]
datadir = "/usr/share/StepMania"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    pisitools.dodir(datadir)

    for i in data:
        fixperms(i)
        shelltools.copytree(i, "%s/%s" % (get.installDIR(), datadir))
