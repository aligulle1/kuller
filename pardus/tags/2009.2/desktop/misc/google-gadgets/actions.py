#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "google-gadgets-for-linux-%s" % get.srcVERSION()

def setup():
    shelltools.export("CXXFLAGS", get.CXXFLAGS().replace("-D_FORTIFY_SOURCE=2", ""))

    #Workaround for compile error with xulrunner 1.9.2 (http://code.google.com/p/google-gadgets-for-linux/issues/detail?id=352)
    shelltools.export("CXXFLAGS", "%s -Wno-invalid-offsetof" % get.CXXFLAGS())

    shelltools.system("sh autotools/bootstrap.sh")
    autotools.configure("--disable-static \
                         --with-browser-plugins-dir=/usr/lib/nsbrowser/plugins \
                         --with-oem-brand=Pardus")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "README")

    #Using system libtool
    pisitools.remove("/usr/lib/libltdl.so*")
    pisitools.remove("/usr/include/ltdl.h")
    pisitools.removeDir("/usr/include/libltdl")
