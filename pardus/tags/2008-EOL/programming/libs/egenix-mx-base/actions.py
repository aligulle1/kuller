#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    pisitools.remove("mx/TextTools/Examples/pytag.py")

def install():
    pythonmodules.install()

    pisitools.dodoc("mx/LICENSE", "mx/COPYRIGHT")
    pisitools.dohtml("mx/Doc/*")
