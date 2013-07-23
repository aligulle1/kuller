#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="OpenJPEG_v1_3"

def setup():
    cmaketools.configure("-DBUILD_SHARED_LIBS=ON -DINCLUDE_INSTALL_DIR=/usr/include")

def build():
    cmaketools.make()

    # docs
    shelltools.cd("doc")
    shelltools.system("doxygen Doxyfile.dox")

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/include/openjpeg","%s/usr/include/*.h" % get.installDIR())
    pisitools.remove("/usr/include/*.h")

    pisitools.dohtml("html/*")
    pisitools.dodoc("ChangeLog")
