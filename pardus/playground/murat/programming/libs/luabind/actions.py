#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "luabind"

def build():
    autotools.make()

def install():
    pisitools.dolib_so("lib/libluabind.so.0.0.0")

    pisitools.insinto("/usr/include/luabind", "luabind/*")

    pisitools.dosym("/usr/lib/libluabind.so.0.0.0", "/usr/lib/libluabind.so.0")
    pisitools.dosym("/usr/lib/libluabind.so.0.0.0", "/usr/lib/libluabind.so")

    pisitools.dohtml("doc/*.html", "doc/*.png")
    pisitools.dodoc("doc/*.txt", "doc/*.rst", "doc/*.ps", "LICENSE")
