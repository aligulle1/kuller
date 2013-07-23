#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def install():
    pisitools.dodir("/opt/RealPlayer")
    shelltools.system("rpm2targz RealPlayer-10.0.8.805-20060718.i586.rpm")
    shelltools.system("tar -zxvf RealPlayer-10.0.8.805-20060718.i586.tar.gz")
    shelltools.cd("usr/local/RealPlayer")
    pisitools.insinto("/usr/kde/3.5/share/icons/hicolor/16x16/apps", "share/icons/realplay_16x16.png", "realplay.png")
    pisitools.insinto("/usr/kde/3.5/share/icons/hicolor/32x32/apps", "share/icons/realplay_32x32.png", "realplay.png")
    pisitools.insinto("/usr/kde/3.5/share/icons/hicolor/48x48/apps", "share/icons/realplay_48x48.png", "realplay.png")
    pisitools.insinto("/usr/share/applications", "share/realplay.desktop")
    pisitools.insinto("/opt/RealPlayer", "LICENSE")
    pisitools.insinto("/opt/RealPlayer", "README")
    pisitools.insinto("/opt/RealPlayer", "postinst")
    pisitools.insinto("/opt/RealPlayer", "plugins")
    pisitools.insinto("/opt/RealPlayer", "common")
    pisitools.insinto("/opt/RealPlayer", "codecs")
    pisitools.insinto("/opt/RealPlayer", "mozilla")
    pisitools.insinto("/opt/RealPlayer", "share")
    pisitools.insinto("/opt/RealPlayer", "lib")
    pisitools.doexe("realplay", "/opt/RealPlayer/")
    pisitools.doexe("realplay.bin", "/opt/RealPlayer/")
    pisitools.dosym("/opt/RealPlayer/realplay", "/usr/bin/realplay")

    shelltools.chmod("%s/opt/RealPlayer/realplay" % get.installDIR())
    shelltools.chmod("%s/opt/RealPlayer/realplay.bin" % get.installDIR())
