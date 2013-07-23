#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "0ad-r09786-alpha"

def setup():
    shelltools.export("pardusCC", get.CC())
    shelltools.export("pardusCXX", get.CXX())
    shelltools.export("pardusCFLAGS", get.CXX())
    shelltools.export("pardusCPPFLAGS", get.CXXFLAGS())

    #shelltools.makedirs("binaries/usr/lib/0ad")

    shelltools.system("./build/workspaces/update-workspaces.sh \
                      --verbose \
                      --with-system-enet \
                      JOBS=%s" % get.makeJOBS())
                      #--bindir=/usr/bin \
                      #--datadir=/usr/share/0ad \
                      #--libdir=/usr/lib/0ad \

def build():
    shelltools.cd("build/workspaces/gcc")
    autotools.make("CONFIG=Release")

def install():
    pisitools.dodoc("LICENSE.txt","license_dbghelp.txt","license_gpl-2.0.txt","license_lgpl-2.1.txt","README.txt")
    pisitools.insinto("/opt/0ad","binaries/*")

    # TRY TO INSTALL 0 A.D. to system path, not under /opt
    #pisitools.insinto("/usr","binaries/usr/*")
    #pisitools.insinto("/usr/share/0ad", "binaries/data/*")

    # Remove static libs - Not so sure about that
    #pisitools.remove("/opt/0ad/system/*.a")

    #pisitools.dosym("/usr/bin/pyrogenesis", "/usr/bin/0ad")
