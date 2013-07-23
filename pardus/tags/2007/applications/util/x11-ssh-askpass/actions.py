#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()
    shelltools.system("xmkmf")

def build():
    shelltools.system("make includes")
    autotools.make()
    
def install():
    pisitools.insinto("/usr/lib/misc", "x11-ssh-askpass")
    pisitools.dosym("/usr/lib/misc/x11-ssh-askpass", "/usr/lib/misc/ssh-askpass")
