#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

dataDir = "/usr/share/cacti"
confDir = "/etc/cacti"
logDir = "/var/log/cacti"
libDir = "/var/lib/cacti"
confFile = "db.config.php"
siteDirs = ["images", "include", "install", "lib", "resource"]
unnecFiles = ["install_windows.html", "install_unix.html", "installation.html", "debug_rpm_installation.html"]

def install():

    for datas in ["*.php", "cacti.sql"]:
        pisitools.insinto(dataDir, datas)

    pisitools.insinto(logDir, "log/*")

    for libs in ["rra", "scripts", "cli"]:
        pisitools.insinto(libDir, libs)

    for d in siteDirs:
        pisitools.insinto(dataDir, d)

    pisitools.domove("%s/include/config.php" % dataDir, confDir, confFile)

    for data in ["poller", "cmd"]:
        shelltools.chmod("%s%s/%s.php" % (get.installDIR(), dataDir, data), 0755)

    shelltools.touch("%s/%s/poller.log" % (get.installDIR(), logDir))

    pisitools.dosym("%s/%s" % (confDir, confFile), "%s/include/config.php" % dataDir)
    pisitools.dosym("%s/rra" % libDir, "%s/rra" % dataDir)
    pisitools.dosym("%s/scripts" % libDir, "%s/scripts" % dataDir)
    pisitools.dosym("%s/cli" % libDir, "%s/cli" % dataDir)
    pisitools.dosym(logDir, "%s/log" % dataDir)
    pisitools.dosym("%s/lib" % dataDir, "%s/lib" % libDir)
    pisitools.dosym("%s/include" % dataDir, "%s/include" % libDir)

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "docs/*")

    for f in unnecFiles:
        pisitools.remove("%s/%s/html/%s" % (get.docDIR(), get.srcNAME(), f))
