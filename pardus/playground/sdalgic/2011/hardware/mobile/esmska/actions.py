#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "kparal-%s-e1e369f" % get.srcNAME()
BASEDIR = "/usr/share/java/esmska"

def build():
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant")

def install():
    shelltools.cd("dist")

    pisitools.insinto(BASEDIR, "esmska.jar")
    pisitools.insinto(BASEDIR, "esmska.sh")
    pisitools.dosym("%s/esmska.sh" % BASEDIR, "/usr/bin/esmska")

    #libs
    pisitools.insinto("%s/lib" %BASEDIR, "lib/*")

    #other files
    #pisitools.dodir("%s/gateways" % BASEDIR)
    #pisitools.insinto("%s/gateways" % BASEDIR, "gateways/*")
    pisitools.insinto(BASEDIR, "gateways")

    #icon
    pisitools.insinto("/usr/share/pixmaps", "icons/esmska.png")

    #esmska conf
    pisitools.insinto("/etc", "esmska.conf")

    #desktop
    shelltools.cd("..")
    pisitools.insinto("/usr/share/applications", "resources/esmska.desktop")

    pisitools.dodoc("README", "dist/license/*" )
