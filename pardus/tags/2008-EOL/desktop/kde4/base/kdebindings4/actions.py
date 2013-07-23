#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="kdebindings-%s" % get.srcVERSION().split("_")[0]

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DBUILD_csharp=OFF -DBUILD_php=OFF", installPrefix="/usr/kde/4", sourceDir="..")
#    cmaketools.configure("-DBUILD_falcon=ON -DENABLE_KROSSFALCON=ON -DBUILD_csharp=OFF -DBUILD_php=OFF", installPrefix="/usr/kde/4", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove pyc files from PyKDE4
    pythonmodules.fixCompiledPy()
    pythonmodules.fixCompiledPy("/usr/kde/4/share/apps/pykde4")

    # pykdeuic4 symlink
    pisitools.dosym("/usr/kde/4/share/apps/pykde4/pykdeuic4.py", "/usr/kde/4/bin/pykde4uic")

    pisitools.dosym("/usr/kde/4/bin/rbqtapi", "/usr/kde/4/bin/rbqt4api")
    pisitools.dosym("/usr/kde/4/bin/rbqtapi", "/usr/kde/4/bin/rbkdeapi")
    pisitools.dosym("/usr/kde/4/bin/rbqtapi", "/usr/kde/4/bin/rbkde4api")
    #pisitools.dosym("/usr/kde/4/bin/rbqtapi", "/usr/kde/4/bin/rbplasmaapi")
