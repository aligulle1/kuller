#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build/build")
    shelltools.cd("%s/%s/build/build" % (get.workDIR(), get.srcDIR()))
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release", sourceDir="..")

def build():
    shelltools.cd("%s/%s/build/build" % (get.workDIR(), get.srcDIR()))
    cmaketools.make()

def install():
    shelltools.cd("%s/%s/build/build" % (get.workDIR(), get.srcDIR()))
    cmaketools.install()

    #shelltools.cd("../../streams")
    #shelltools.system("python build_streams.py")

    #pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
