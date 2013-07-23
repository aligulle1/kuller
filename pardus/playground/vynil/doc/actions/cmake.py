#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

WorkDir = ""

def setup():
    cmake.configure()

def build():
    cmake.make()

def install():
    cmake.install()

    pisitools.dodoc("CHANGELOG", "README", "TODO", "KNOWN_BUGS", "doc/*")
