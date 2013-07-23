#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "cmcurl-r117"

def setup():
    cmaketools.configure("-DCMAKE_SKIP_RPATH=ON")

def build():
    cmaketools.make()

def install():
    pisitools.dodoc("curl.copyright")

    shelltools.copy("slicerlibcurl/*", "%s/usr/include/slicerlibcurl" % get.installDIR())

    pisitools.insinto("/usr/include/slicerlibcurl", "*.h")

    pisitools.dodir("/usr/lib/slicerlibcurl-7.12.1")
    pisitools.insinto("/usr/lib/slicerlibcurl-7.12.1", "bin/libslicerlibcurl.a")
    pisitools.insinto("/usr/lib/slicerlibcurl-7.12.1", "CMake/UseSLICERLIBCURL.cmake")
    pisitools.insinto("/usr/lib/slicerlibcurl-7.12.1", "CMake/SLICERLIBCURLConfig.cmake.in")
