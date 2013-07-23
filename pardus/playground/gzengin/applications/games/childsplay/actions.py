#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def install():
    shelltools.system("mv -f /var/cache/pisi/archives/childsplay-0.90.2.tar.bz2 ./")
    shelltools.system("tar -xjvf childsplay-0.90.2.tar.bz2")
    pisitools.insinto("/", "usr")
    shelltools.system("rm -rf *")