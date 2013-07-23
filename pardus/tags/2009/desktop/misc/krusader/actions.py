#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="krusader-%s" % get.srcVERSION().replace("_","-")

def setup():
    cmaketools.configure(installPrefix="/usr/kde/4",sourceDir=".")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/share/icons/hicolor/48x48/apps/krusader_user.png", "/usr/share/icons/hicolor/48x48/apps/krusader.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "FAQ")
