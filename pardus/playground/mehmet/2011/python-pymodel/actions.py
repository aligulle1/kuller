#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

instalDir = "/usr/lib/python2.7/site-packages"

def install():
    pythonmodules.install()

    pisitools.insinto("%s/python-pymodel" % instalDir, "pymodel/*")

    for binary in ["pma.py", "pmg.py", "pmt.py", "trun.py", "dotsvg", \
            "clogdiff", "tpath", "dotps", "wsgirunner.py"]:
        pisitools.dosym("%s/python-pymodel/%s" % (instalDir, binary), \
                "/usr/bin/%s" % binary)

    pisitools.insinto("/usr/share/doc/python-pymodel", "samples")
    pisitools.insinto("/usr/share/doc/python-pymodel", "notes")
