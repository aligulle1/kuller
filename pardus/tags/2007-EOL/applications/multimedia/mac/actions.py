#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = 'mac-3.99-u4-b5'

def setup():
    autotools.configure('--disable-static')

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "README", "ChangeLog", "NEWS", "TODO", "src/Credits.txt", "src/History.txt")
    pisitools.dohtml("src/LICENSE.htm", "src/Readme.htm")
