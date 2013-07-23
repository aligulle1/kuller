#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "CableSwig-ITK-%s" % get.srcVERSION()

def setup():
    cmaketools.configure("-DCMAKE_SKIP_RPATH=ON")

def build():
    cmaketools.make()

def install():
    pisitools.dobin("bin/cableidx")
    pisitools.dobin("bin/cswig")

    pisitools.dodoc("SWIG/Doc/Devel/*", "SWIG/Doc/Manual/*", "README")

    pisitools.insinto("/usr/lib/CableSwig/SWIGLib", "SWIG/Lib/*.i")
    pisitools.insinto("/usr/lib/CableSwig/SWIGLib", "SWIG/Lib/*.swg")
    pisitools.insinto("/usr/lib/CableSwig/SWIGLib/java", "SWIG/Lib/java/*.i")
    pisitools.insinto("/usr/lib/CableSwig/SWIGLib/java", "SWIG/Lib/java/*.swg")
    pisitools.insinto("/usr/lib/CableSwig/SWIGLib/python", "SWIG/Lib/python/*.i")
    pisitools.insinto("/usr/lib/CableSwig/SWIGLib/python", "SWIG/Lib/python/*.swg")
    pisitools.insinto("/usr/lib/CableSwig/SWIGLib/tcl", "SWIG/Lib/tcl/*.i")
    pisitools.insinto("/usr/lib/CableSwig/SWIGLib/tcl", "SWIG/Lib/tcl/*.swg")

    pisitools.dosed("InstallOnly/CableSwigConfig.cmake", "/usr/lib/CableSwig/bin/gccxml", "/usr/bin/gccxml")
    pisitools.insinto("/usr/lib/CableSwig/", "InstallOnly/CableSwigConfig.cmake")
