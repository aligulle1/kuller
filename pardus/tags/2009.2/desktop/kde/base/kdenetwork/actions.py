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
NoStrip=["/usr/kde/4/share", "/usr/share"]

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DWITH_JINGLE=TRUE", installPrefix="/usr/kde/4",sourceDir="..")

def build():
    shelltools.cd("build")

    #parallel compilation seems broken since 4.4.4
    cmaketools.make("-j1")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #shelltools.chmod("%s/kopete/kopete/kconf_update/kopete-update_yahoo_server.pl" % get.installDIR(), 0755)
