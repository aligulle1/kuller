#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dodir("/opt/skype")
    pisitools.dodir("/opt/skype/sound")

    pisitools.doexe("skype", "/opt/skype")
    pisitools.dosym("/opt/skype/skype", "/usr/bin/skype")

    pisitools.insinto("/opt/skype/sounds", "sounds/*.wav")
    pisitools.insinto("/etc/dbus-1/system.d", "skype.conf")

    pisitools.insinto("/usr/kde/3.5/share/icons/hicolor/16x16/apps", "icons/skype_16_32.png", "skype.png")
    pisitools.insinto("/usr/kde/3.5/share/icons/hicolor/32x32/apps", "icons/skype_32_32.png", "skype.png")
    pisitools.insinto("/usr/kde/3.5/share/icons/hicolor/48x48/apps", "icons/skype_48_32.png", "skype.png")

    pisitools.dodoc("README", "LICENSE")
