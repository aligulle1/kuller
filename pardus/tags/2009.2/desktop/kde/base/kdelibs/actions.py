#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

NoStrip=["/usr/kde/4/share", "/usr/share/icons"]
shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DICON_INSTALL_DIR=\"/usr/share/icons\" \
                          -DKDE4_ENABLE_FINAL=ON \
                          -DSYSCONF_INSTALL_DIR=/etc \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DDBUS_SYSTEM_SERVICES_INSTALL_DIR=/usr/share/dbus-1/system-services \
                          -DKDE_DEFAULT_HOME=.kde4 \
                          -DKDE_DISTRIBUTION_TEXT=\"Pardus\"", installPrefix="/usr/kde/4", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    #Workaround for prefix difference of Policykit and KDE
    #pisitools.dodir("/usr/share/PolicyKit/policy")
    #pisitools.dosym("../../../../share/PolicyKit/policy", "/usr/kde/4/share/PolicyKit/policy")
    #this workaround doesn't work since YALI does not install packages in order

    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #move Qt Designer plugins to Qt plugin directory
    pisitools.dodir("/usr/qt/4/plugins/designer")
    pisitools.domove("/usr/kde/4/lib/kde4/plugins/designer/*", "/usr/qt/4/plugins/designer")
    pisitools.removeDir("/usr/kde/4/lib/kde4/plugins/designer")

    #Use openssl CA list instead of the outdated KDE list
    pisitools.remove("/usr/kde/4/share/apps/kssl/ca-bundle.crt")
    pisitools.dosym("/etc/ssl/certs/ca-bundle.crt", "/usr/kde/4/share/apps/kssl/ca-bundle.crt")
