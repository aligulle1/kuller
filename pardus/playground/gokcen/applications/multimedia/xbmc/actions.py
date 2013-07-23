#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "XBMC"

def setup():
    #make configure scripts executable
    for root, dirs, files in os.walk(get.workDIR()):
        for name in files:
            if name == "configure":
                shelltools.chmod(os.path.join(root, name))
    shelltools.chmod("xbmc/cores/dvdplayer/Codecs/ffmpeg/doc/texi2pod.pl")

    pisitools.dosed("xbmc/utils/CharsetConverter.h", "fribidi/fribidi_char_sets.h", "fribidi/fribidi-char-sets.h")
    pisitools.dosed("xbmc/utils/ArabicShaping.h", "fribidi/fribidi_char_sets.h", "fribidi/fribidi-char-sets.h")
    pisitools.dosed("xbmc/utils/ArabicShaping.cpp", "FRIBIDI_TRUE", "1")
    pisitools.dosed("xbmc/utils/ArabicShaping.cpp", "FRIBIDI_FALSE", "0")

    autotools.autoconf() #to fix buggy mktime check
    autotools.configure("--disable-debug")

def build():
    autotools.make()

def install():
    xbmcDir = "/usr/share/xbmc"

    pisitools.dodir(xbmcDir)
    for fl in ["xbmc.bin", "xbmc-xrandr"]:
        shelltools.copy(fl, "%s/usr/share/xbmc/" % get.installDIR())
    pisitools.dodir("/usr/bin")
    shelltools.copy("tools/Linux/xbmc.sh", "%s/usr/bin/xbmc" % get.installDIR())
    shelltools.chmod("%s/usr/bin/xbmc" % get.installDIR())

    #copy data files
    for dir in ["language", "media", "screensavers", "scripts", "skin", "sounds", "userdata", "visualisations", "system"]:
        shelltools.copytree(dir, "%s/usr/share/xbmc" % get.installDIR())

    #install web server
    pisitools.dodir("/usr/share/xbmc/web")
    shelltools.system("/usr/bin/unzip -oq web/Project_Mayhem_III_webserver_v1.0.zip -d %s/usr/share/xbmc/web" % get.installDIR())

    #remove .so and .dlls
    shelltools.unlinkDir("%s/usr/share/xbmc/system/players" % get.installDIR())
    shelltools.unlinkDir("%s/usr/share/xbmc/system/cdrip" % get.installDIR())
    for root, dirs, files in os.walk(get.installDIR()):
        for name in files:
            lname = name.lower()
            if lname.endswith(".so") or lname.endswith(".dll") or lname.endswith(".a"):
                shelltools.unlink(os.path.join(root, name))

    pisitools.dodoc("*.txt", "README.linux", "LICENSE.GPL")
