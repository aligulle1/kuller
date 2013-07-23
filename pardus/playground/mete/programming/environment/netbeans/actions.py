#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
import os

WorkDir = "."

def setup():
    pass

def fixPermissions():
    import os
    for root, dirs, files in os.walk("%s/opt" % get.installDIR()):
        for d in dirs:
            shelltools.system("/bin/chmod 0755 %s/%s" % (root, d))
        for f in files:
            shelltools.system("/bin/chmod 0644 %s/%s" % (root, f))

def build():
    shelltools.makedirs("%s/nbbuild/ergonomics_build_fix" % get.workDIR())
    shelltools.export("JAVA_HOME", "/opt/sun-jdk5")
    shelltools.export("DISPLAY", ":0.0")
    shelltools.system("ant -Djava.awt.headless=true -Dergonomic.clusters.extra=%s/nbbuild/ergonomics_build_fix -f %s/nbbuild/build.xml build-nozip" % (get.workDIR(), get.workDIR()))

    # Remove non-Linux binaries
    nonLinuxFiles=("exe","cmd","bat","dll")

    for root, dirs, files in os.walk(os.path.join(get.workDIR(), "/nbbuild/netbeans")):
        for name in dirs:
            for nonLinux in nonLinuxFiles:
                pisitools.remove(os.path.join(root, name) + "*.%s" % nonLinux)

    pisitools.dosym("%s/nbbuild/netbeans/bin/netbeans" % get.workDIR(), "/usr/bin/netbeans")
    pisitools.remove("%s/nbbuild/netbeans/cnd2/bin/*-SunOS-*" % get.workDIR())
    pisitools.remove("%s/nbbuild/netbeans/cnd2/bin/*-Mac_OS_X-*" % get.workDIR())
    pisitools.remove("%s/nbbuild/netbeans/ide11/docs/*.zip" % get.workDIR())
    pisitools.remove("%s/nbbuild/netbeans/javadoc/*.zip" % get.workDIR())
    pisitools.remove("%s/nbbuild/netbeans/nb.cluster.*" % get.workDIR())
    pisitools.remove("%s/nbbuild/netbeans/*.built" % get.workDIR())
    pisitools.remove("%s/nbbuild/netbeans/moduleCluster.properties" % get.workDIR())
    pisitools.remove("%s/nbbuild/netbeans/module_tracking.xml" % get.workDIR())
    pisitools.remove("%S/nbbuild/netbeans/build_info" % get.workDIR())



def install():
    pisitools.dodir("/opt/netbeans")

    shelltools.copytree("%s/nbbuild/netbeans/*" % get.workDIR(), "%s/opt/netbeans/" % get.installDIR())
    shelltools.sym("/opt/nb6.7/netbeans.png", "/usr/share/icons/hicolor/32x32/apps/netbeans.png")

    for doc in ["LICENSE.txt", "LEGALNOTICE.txt", "DISTRIBUTION.txt", "THIRDPARTYLICENSE.txt", "README.html"]:
        file = "%s/opt/netbeans/%s" % (get.installDIR(),doc)
        pisitools.dodoc(file)
        shelltools.unlink(file)

    fixPermissions()
