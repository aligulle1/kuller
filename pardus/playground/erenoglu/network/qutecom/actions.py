#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "-"))
WorkDir = "qutecom-2-2-076775b98c8c"

def setup():
    shelltools.makedirs("buildnew")
    shelltools.cd("buildnew")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Debug", sourceDir="..")

def build():
    shelltools.cd("buildnew")
    cmaketools.make()

def install():
    shelltools.cd("buildnew")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
#    cmaketools.install()
    shelltools.cd("..")
    pisitools.dodoc("COPYING", "README")
