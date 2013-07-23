#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure","python2.4", get.curPYTHON())
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pythonmodules.fixCompiledPy()

    pisitools.dodoc("AUTHORS", "NEWS", "ChangeLog")
