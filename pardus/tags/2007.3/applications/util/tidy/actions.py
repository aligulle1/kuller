#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "tidy-%s" % get.srcVERSION().split("_", 1)[1]

def setup():
    shelltools.system("sh build/gnuauto/setup.sh")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
