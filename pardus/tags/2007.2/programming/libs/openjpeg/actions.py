#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="OpenJPEG"

def setup():
    cmaketools.configure("-DBUILD_SHARED_LIBS=ON")

def build():
    cmaketools.make()

    # docs
    shelltools.cd("doc")
    shelltools.system("doxygen Doxyfile.dox")

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/include/openjpeg","%s/usr/include/*.h" % get.installDIR())
    pisitools.remove("/usr/include/*.h")

    pisitools.dodoc("ChangeLog")
    pisitools.dohtml("html/*")
