#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    shelltools.system("mv -f /var/cache/pisi/archives/easymp3gain-gtk2_0.4.2.tar.bz2 ./")
    shelltools.system("tar -xjvf easymp3gain-gtk2_0.4.2.tar.bz2")
    pisitools.insinto("/", "usr")
    pisitools.dosym("/usr/share/easymp3gain-gtk/easymp3gain", "/bin/easymp3gain")
    shelltools.system("rm -rf *")