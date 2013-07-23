#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir = "Qemulator-0.5"

def install():
    pisitools.insinto("/usr/lib/qemulator", "usr/local/lib/qemulator/*")
    pisitools.insinto("/usr/share", "usr/local/share/*")
    pisitools.dosym("/usr/lib/qemulator/qemulator.py", "/usr/bin/qemulator")

    pisitools.dodoc("LICENCE", "README")

