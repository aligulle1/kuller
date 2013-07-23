#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ReviewBoard-1.1alpha2"

def setup():
    # Avoid trying to bootstrap setup.py; we have this via PISI
    pisitools.dosed("setup.py", "^from ez_setup", "#from ez_setup")
    pisitools.dosed("setup.py", "^use_setuptools()", "#use_setuptools()")

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

