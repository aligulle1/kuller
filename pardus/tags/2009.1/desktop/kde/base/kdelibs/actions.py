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

NoStrip=["/usr/kde/4/share", "/usr/share/icons"]
shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DICON_INSTALL_DIR=\"/usr/share/icons\" -D_KDE_DEFAULT_HOME_POSTFIX=4", installPrefix="/usr/kde/4", sourceDir="..")
#    cmaketools.configure("-DKDE4_ENABLE_FINAL=ON -D_KDE_DEFAULT_HOME_POSTFIX=4",installPrefix="/usr/kde/4",sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #move Qt Designer plugins to Qt plugin directory
    pisitools.dodir("/usr/qt/4/plugins/designer")
    pisitools.domove("/usr/kde/4/lib/kde4/plugins/designer/*", "/usr/qt/4/plugins/designer")
    pisitools.removeDir("/usr/kde/4/lib/kde4/plugins/designer")

    #Use openssl CA list instead of the outdated KDE list
    pisitools.remove("/usr/kde/4/share/apps/kssl/ca-bundle.crt")
    pisitools.dosym("/etc/ssl/certs/ca-bundle.crt", "/usr/kde/4/share/apps/kssl/ca-bundle.crt")
