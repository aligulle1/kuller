#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(),get.srcNAME())

def setup():
    qt4.configure("qtmindmap.pro")

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.dodoc("README")
