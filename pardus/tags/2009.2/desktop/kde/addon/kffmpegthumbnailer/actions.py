#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure(installPrefix=get.kdeDIR())

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("Changelog", "COPYRIGHT", "README")
