#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir="wbar-pardus_patched-" + get.srcVERSION()

def build():
    shelltools.system("make")

def install():
    shelltools.system("make install")
    pisitools.dodoc("AUTHORS","COPYING","NEWS","README")