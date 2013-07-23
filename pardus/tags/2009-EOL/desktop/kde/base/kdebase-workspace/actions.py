#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
NoStrip=["/usr/kde/4/share", "/usr/share"]

import os

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    # PAM files are named kde4.pam and kde4-np.pam. We should change cmake file to make PAM modules work
    cmaketools.configure("-DKDE4_COMMON_PAM_SERVICE=kde4 \
                          -DKDE4_ENABLE_FINAL=1 \
                          -DDBUS_SYSTEM_SERVICES_INSTALL_DIR=/usr/share/dbus-1/system-services \
                          -DKDE4_KCHECKPASS_PAM_SERVICE=kde4", installPrefix="/usr/kde/4",sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")

    # Do not use existing system KDM while creating the new one
    shelltools.export("GENKDMCONF_FLAGS", "--no-old")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Copy desktop files into xsessions directory
    pisitools.insinto("/usr/share/xsessions", "kdm/kfrontend/sessions/kde*.desktop")

    # Put kdmrc into /etc/X11/kdm, so it can be modified on live CDs
    pisitools.domove("/usr/kde/4/share/config/kdm/kdmrc", "/etc/X11/kdm/", "kdmrc")
    pisitools.dosym("/etc/X11/kdm/kdmrc", "/usr/kde/4/share/config/kdm/kdmrc")

    # Use common Xsession script
    pisitools.remove("/usr/kde/4/share/config/kdm/Xsession")
    pisitools.dosym("/usr/lib/X11/xinit/Xsession", "/usr/kde/4/share/config/kdm/Xsession")

    # Remove upd file for 4.2-4.3 switch, we'll do this in startkde to not effect working plasma of 4.2
    pisitools.remove("/usr/kde/4/share/apps/kconf_update/plasmarc-to-plasmadesktoprc.upd")
    pisitools.remove("/usr/kde/4/lib/kconf_update_bin/plasma-to-plasma-desktop")

    #move this to /usr/share/PolicyKit/policy
    if os.path.isdir("%s/usr/kde/4/share/PolicyKit/policy" % get.installDIR()):
        pisitools.dodir("/usr/share/PolicyKit")
        pisitools.domove("/usr/kde/4/share/PolicyKit/policy/", "/usr/share/PolicyKit")
        os.removedirs("%s/usr/kde/4/share/PolicyKit" % get.installDIR())

