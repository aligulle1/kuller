#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

runDir = "/var/run/wt"

def setup():
    pisitools.dosed("wt_config.xml", r"<run-directory>.*</run-directory>", "<run-directory>%s</run-directory>" % runDir)

    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DMXML_SUPPLIED=ON \
                          -DCONNECTOR_FCGI=OFF \
                          -DCONNECTOR_HTTP=ON \
                          -DMULTI_THREADED=ON \
                          -DRUNDIR=%s%s" % (get.installDIR(), runDir),
                         sourceDir = "..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "LICENSE", "ReleaseNotes.html")
