#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("CMakeLists.txt", "{WINSOCK}", "{WINSOCK} -lutil")
    pisitools.dosed("src/util/funcs.cpp", "\"data\"", "\"/usr/share/paintown/\"")

    #Use sytem's hawknl
    #pisitools.dosed("src/network/network.h", "\"hawknl/nl.h\"", "<nl.h>")
    #pisitools.dosed("src/network/network.cpp", "\"hawknl/nl.h\"", "<nl.h>")

    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("--disable-static -Wno-dev", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    pisitools.dobin("build/bin/paintown")
    pisitools.insinto("/usr/share/paintown/", "data/*")

    pisitools.dodoc("LICENSE", "LEGAL", "TODO", "README")
