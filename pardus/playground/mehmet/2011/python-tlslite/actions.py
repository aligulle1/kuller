#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    #workdir = "%s/tlslite-%s" % (get.workDIR(), get.srcVERSION())
    dirs = ["docs", "docs/public", "docs/private"]
    for d in dirs:
        #shelltools.chmod("%s/%s/*" % (workdir, d), 0644)
        shelltools.chmod("%s/*" % (d), 0644)
    pisitools.insinto("/usr/share/doc/python-tlslite", "docs/*")
