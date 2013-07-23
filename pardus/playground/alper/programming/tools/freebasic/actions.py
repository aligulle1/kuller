#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "FreeBASIC"

def install():
    pisitools.dobin("fbc")

    pisitools.insinto("/usr/share/freebasic/bin/linux", "bin/linux/*")
    pisitools.insinto("/usr/share/freebasic/lib/", "lib/linux/*")
    pisitools.insinto("/usr/share/freebasic/inc/", "inc/*")

    pisitools.dodoc("readme.txt", "changelog.txt", "migrating.txt", "docs/*")
