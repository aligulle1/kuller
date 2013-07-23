#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir='./'
NoStrip='/'
DesktopDir='%s/share/applications/kde' % get.kdeDIR()
InstallDesktopDir='%s/%s' % (get.installDIR(),DesktopDir)

Modules = {"kthememanager": ["X-KDE-settings-looknfeel;", "X-KDE-tasma-looknfeel"],
           "kcmsmserver": ["X-KDE-settings-components;", "X-KDE-tasma-desktop"],
           "kcmkrfb": ["X-KDE-settings-network;", "X-KDE-tasma-network"],
           "joystick": ["X-KDE-settings-hardware;", "X-KDE-tasma-peripherals"],
           "kcmlirc": ["X-KDE-settings-peripherals;", "X-KDE-tasma-peripherals"],
           "kcmktalkd": ["X-KDE-settings-network;", "X-KDE-tasma-network"],
           "kcmperformance": ["X-KDE-settings-components;", "X-KDE-tasma-desktop"],
           "media": ["X-KDE-settings-peripherals;", "X-KDE-tasma-peripherals"],
           "kcmlaunch": ["X-KDE-settings-looknfeel;", "X-KDE-tasma-looknfeel"],
           "bell": ["X-KDE-settings-sound;", "X-KDE-tasma-sound"],
           "kwallet-config": ["X-KDE-settings-security;", "X-KDE-tasma-desktop"],
           "spellchecking": ["X-KDE-settings-components;", "X-KDE-tasma-desktop"],
           "desktoppath": ["X-KDE-settings-system;", "X-KDE-tasma-desktop"],
           "audiocd": ["X-KDE-settings-sound;", "X-KDE-tasma-sound"]}

def install():
    shelltools.makedirs(InstallDesktopDir)

    for i in Modules.keys():
        shelltools.copy("%s/%s.desktop" % (DesktopDir, i), "%s/tasma%s.desktop" % (InstallDesktopDir, i))
        pisitools.dosed("%s/tasma%s.desktop" % (InstallDesktopDir, i), Modules[i][0], "%s%s" % (Modules[i][0], Modules[i][1]))

    # Documentation
    shelltools.echo("README", "Extra Tasma Modules")
    shelltools.echo("ChangeLog", "First Release - 15 Aug 2007")
    pisitools.newdoc("gpl-2.0.txt", "COPYING")
    pisitools.dodoc("README", "ChangeLog")
