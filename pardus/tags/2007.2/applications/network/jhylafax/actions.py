#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = ''

def install():
    pisitools.insinto("/usr/share/jhylafax", "jhylafax-1.3.9-app.jar")
