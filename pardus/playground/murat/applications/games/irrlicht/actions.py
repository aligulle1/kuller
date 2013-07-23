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

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    shelltools.unlinkDir("examples/Demo")
    shelltools.unlinkDir("examples/14.Win32Window")

    for files in ["examples/buildAllExamples.sh", "examples/BuildAllExamples.sln",
                  "examples/BuildAllExamples_v7.sln", "examples/whereAreTheBinaries.txt", "bin/Linux/readme.txt"]:
        shelltools.unlink(files)

def build():
    shelltools.cd("source/Irrlicht")
    autotools.make("sharedlib")

    shelltools.cd("../../tools/GUIEditor")
    autotools.make()

    shelltools.cd("../IrrFontTool/newFontTool")
    autotools.make()

    shelltools.cd("../../../examples")
    for dirs in os.listdir("."):
        shelltools.cd(dirs)
        autotools.make()
        shelltools.cd("..")

def install():
    shelltools.cd("source/Irrlicht")
    autotools.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../..")

    fixperms("media")
    pisitools.insinto("/usr/share/irrlicht", "media/*")

    fixperms("include")
    pisitools.insinto("/usr/include/irrlicht", "include/*")

    pisitools.dobin("tools/GUIEditor/irrlicht-GUIEditor")
    pisitools.dobin("bin/Linux/*")

    pisitools.dodoc("*.txt", "doc/irrlicht.chm", "doc/*.txt")

    for docs in os.listdir("examples"):
        if os.path.exists("examples/%s/tutorial.html" % docs):
            pisitools.insinto("/usr/share/doc/%s/examples/%s" % (get.srcTAG(), docs), "examples/%s/tutorial.html" % docs)
