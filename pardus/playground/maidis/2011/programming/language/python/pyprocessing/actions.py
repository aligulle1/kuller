#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir = "pyprocessing"

def build():
    # must be on X and use --ignore-sandbox
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("README.txt")
