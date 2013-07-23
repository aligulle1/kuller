#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="reportlab_2_1/reportlab"

def install():
    pythonmodules.install()

    for doc in ["docs/*","demos","changes","README","license.txt"]:
        pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), doc)
