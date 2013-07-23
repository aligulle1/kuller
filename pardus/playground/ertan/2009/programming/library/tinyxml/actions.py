#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "tinyxml"

def build():
    pisitools.dosed("Makefile", "pardus_cflags", "%s" % get.CFLAGS()) 
    autotools.make()
    shelltools.system("g++ -fPIC -shared -o libtinyxml.so.0.%s -Wl,-soname,libtinyxml.so.0 *.o" % get.srcVERSION())

def install():
    pisitools.insinto("/usr/include", "*.h")
    pisitools.dolib("libtinyxml.so.0.%s" % get.srcVERSION())
    pisitools.dosym("/usr/lib/libtinyxml.so.0.%s" % get.srcVERSION(), "/usr/lib/libtinyxml.so.0")
    pisitools.dosym("/usr/lib/libtinyxml.so.0.%s" % get.srcVERSION(), "/usr/lib/libtinyxml.so")
    pisitools.dodoc("changes.txt", "readme.txt")
    pisitools.dohtml("docs/*")
