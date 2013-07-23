#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "salatinoid"
shelltools.export("HOME", "%s" % get.workDIR())

def setup():
    shelltools.cd("applet")
    cmaketools.configure(installPrefix="/usr/kde/4", sourceDir=".")

    shelltools.cd("../dataengine")
    cmaketools.configure(installPrefix="/usr/kde/4", sourceDir=".")

def build():
    shelltools.cd("applet")
    cmaketools.make()

    shelltools.cd("../dataengine")
    cmaketools.make()

def install():
    shelltools.cd("applet")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../dataengine")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
