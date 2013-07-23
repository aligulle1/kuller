#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="kdebase-runtime-%s" % get.srcVERSION().split("_")[0]
NoStrip = ["/usr/kde/4/share/"]

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure(installPrefix="/usr/kde/4", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #delete kmplayer icons from oxygen theme
    prefix = "/usr/kde/4/share/icons/oxygen/"
    conflictingIcons = ("kmplayer", "digikam", "showfoto")

    for size in (16, 22, 32, 48, 64, 128):
        for icon in conflictingIcons:
            pisitools.remove("%s%sx%s/apps/%s.png" % (prefix, size, size, icon))

    for icon in conflictingIcons:
        pisitools.remove("%sscalable/apps/%s.svgz" % (prefix, icon))
