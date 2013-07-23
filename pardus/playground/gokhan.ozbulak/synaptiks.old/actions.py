#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde4
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def setup():
    kde4.configure("-DWITH_XINPUT2=ON")

def build():
    kde4.make()

def install():
    kde4.install()
