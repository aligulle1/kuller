#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
NoStrip=["/usr/kde/4/share", "/usr/share/icons"]

def setup():
    for d in ["ksysv","lilo-config","kuser","kpackage","knetworkconf"]:
        shelltools.unlinkDir(d)

    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DICON_INSTALL_DIR=\"/usr/share/icons\"", installPrefix="/usr/kde/4",sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
