#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "amarok-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("src/collection/CMakeLists.txt", 'add_subdirectory\( mtp', '#add_subdirectory( mtp')
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release -DMTP_FOUND=FALSE -DCMAKE_BUILD_TYPE=debugfull", installPrefix="/usr/kde/4", sourceDir=".")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "README", "COPYING", "ChangeLog")
