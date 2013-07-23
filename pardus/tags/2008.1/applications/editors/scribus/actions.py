#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE -DCMAKE_SKIP_RPATH=TRUE \
                          -DLIB_INSTALL_DIR=%s -DWANT_CAIRO=1 -DMIMELNKDIR=%s/%s" % ("/usr/lib/", get.kdeDIR(), "share/mimelnk/application/"))

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/share/doc/scribus", "/usr/share/doc/", "%s-%s" % (get.srcNAME(), get.srcVERSION()))
    pisitools.insinto("/usr/share/pixmaps", "scribus/icons/scribusicon.png")
