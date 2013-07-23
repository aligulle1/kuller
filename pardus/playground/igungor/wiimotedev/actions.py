#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-project-%s" % (get.srcNAME(), get.srcVERSION().split("_")[0])


def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DUSE_STATIC_CWIID=OFF", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make("VERBOSE=3")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("../CHANGELOG", "../COPYING", "../README")
