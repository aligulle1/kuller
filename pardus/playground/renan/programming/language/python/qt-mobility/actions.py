#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import qt4
def setup():
    autotools.rawConfigure("-prefix %s \
                        -libdir %s \
                        -plugindir %s \
                        -examplesdir %s \
                        -demosdir %s \
                        " % (qt4.prefix, qt4.libdir, qt4.plugindir, qt4.examplesdir, qt4.demosdir))

def build():
    autotools.make()

def install():
    autotools.Install()
