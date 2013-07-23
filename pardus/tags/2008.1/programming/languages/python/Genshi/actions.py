#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

examples = "%s/%s/examples" % (get.docDIR(), get.srcTAG())
htmltxt = "%s/%s/html" % (get.docDIR(), get.srcTAG())

def setup():
    shelltools.chmod("examples/*", 0644)

def install():
    pythonmodules.install() 

    pisitools.dohtml("doc/")
    pisitools.insinto(examples, "examples/*")
    pisitools.insinto(htmltxt, "doc/*.txt")

    pisitools.dodoc("README.txt", "COPYING", "ChangeLog")
