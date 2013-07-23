#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = 'avidemux_2.3.0'

def setup():
    autotools.configure("--with-jsapi-include=/usr/include/js")

def build():
    autotools.make("-j1")

def install():
    autotools.install()
    
    pisitools.insinto("/usr/share/pixmaps", "avidemux_icon.png", "avidemux.png")

    pisitools.dodoc("COPYING", "History", "AUTHORS", "ChangeLog")
