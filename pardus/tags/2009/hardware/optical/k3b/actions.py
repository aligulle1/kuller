#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008,2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().split("_")[0])

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DNEWFFMPEGAVCODECPATH=ON", installPrefix="/usr/kde/4", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")

    pisitools.domo("k3b.po", "tr", "k3b.mo")
    pisitools.dodir("/usr/kde/4/share/locale/tr/LC_MESSAGES")
    pisitools.domove("/usr/share/locale/tr/LC_MESSAGES/k3b.mo", "/usr/kde/4/share/locale/tr/LC_MESSAGES")
    pisitools.removeDir("/usr/share/locale")
