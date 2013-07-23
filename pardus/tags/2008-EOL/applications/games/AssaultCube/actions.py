#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "AssaultCube_v%s" % get.srcVERSION()
datadirs = ["bot", "config", "packages"]
src = "source/src"
target = "/usr/share/AssaultCube"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    pisitools.dosed("%s/Makefile" % src, "strip", "#strip")

    for d in datadirs:
        fixperms(d)

    fixperms("docs")

def build():
    shelltools.cd(src)
    autotools.make('CXXOPTFLAGS="%s -fomit-frame-pointer" -j1' % get.CXXFLAGS())

def install():
    pisitools.dodir(target)
    for d in datadirs:
        shelltools.copytree(d, "%s/%s" % (get.installDIR(), target))

    for f in ["ac_client", "ac_server"]:
        pisitools.dobin("source/src/%s" % f, target)

    pisitools.dodoc("source/AUTHORS", "source/LICENSE", "source/*.txt", "README.html", "icon.ico")
    shelltools.copytree("docs", "%s/%s/%s" % (get.installDIR(), get.docDIR(), get.srcTAG()))

    # We will add our version as additional file
    pisitools.remove("/usr/share/AssaultCube/config/maprot.cfg")

