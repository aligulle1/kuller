#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s" % get.srcNAME()

def install():

    #Remove scripts which are conflicted with gimp
    for script in ("slide", "addborder", "erase-rows", "coffee", "fuzzyborder", "add-bevel"):
        shelltools.unlink("%s.scm" % script)

    pisitools.insinto("/usr/share/gimp/2.0/scripts/", "*.scm")
    pisitools.insinto("/usr/share/gimp/2.0/gimpressionist/Presets/", "Presets/*")

    pisitools.dodoc("README.txt")
