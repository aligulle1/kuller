#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules

def setup():
    autotools.configure()

def build():
    autotools.make()
    shelltools.cd("python")
    pythonmodules.compile()
    shelltools.cd("..")

def install():
    autotools.install()
    shelltools.cd("python")
    pythonmodules.install()
