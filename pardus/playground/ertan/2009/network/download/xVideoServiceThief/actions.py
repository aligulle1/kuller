#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def setup():
    # fix translations
    shelltools.move("resources/translations/xVST_cz.ts", "%s/resources/translations/xVST_cs.ts" % get.workDIR())
    shelltools.move("resources/translations/xVST_jp.ts", "%s/resources/translations/xVST_ja.ts" % get.workDIR()) 
    shelltools.move("resources/translations/xVST_du.ts", "%s/resources/translations/xVST_nl.ts" % get.workDIR())

    shelltools.system("qmake-qt4")  

def build():
    autotools.make()

def install():
    shelltools.system("lrelease-qt4 resources/translations/*.ts")

    pisitools.dobin("bin/xvst")
    pisitools.insinto("/usr/share/xVideoServiceThief/languages/", "resources/translations/*.qm")
    pisitools.insinto("/usr/share/xVideoServiceThief/languages/", "resources/translations/definitions/*.language")
    shelltools.chmod("%s/usr/share/xVideoServiceThief/languages/*.language" % get.installDIR(), 0644)
    shelltools.chmod("resources/images/InformationLogo.png", 0644)
    pisitools.insinto("/usr/share/pixmaps", "resources/images/InformationLogo.png", "xvst.png")

    import os

    for root, dirs, files in os.walk("%s/resources/services" % get.workDIR()):
        for name in files:
            if name.endswith(".js"):
                pisitools.insinto("/usr/share/xVideoServiceThief/plugins", os.path.join(root, name))

    shelltools.chmod("%s/usr/share/xVideoServiceThief/plugins/*" % get.installDIR(), 0755)


