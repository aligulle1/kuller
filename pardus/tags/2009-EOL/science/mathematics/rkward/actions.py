#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_BUILD_TYPE=release -DR_HOME=/usr/lib/R", installPrefix="/usr/kde/4",sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    #for installing rbackend mkdir needed directory(for R-2.5.0)
    pisitools.dodir("/usr/lib/R/library")

    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # TODO: this one seems better than the one in kdelibs
    pisitools.remove("%s/share/apps/katepart/syntax/r.xml" % get.kdeDIR())

    # Fix conflict with R
    pisitools.remove("/usr/lib/R/library/R.css")
