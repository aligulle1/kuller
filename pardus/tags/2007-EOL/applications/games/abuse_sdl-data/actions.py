#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get 


WorkDir = "./"

def install():
    pisitools.dodir("/usr/share/abuse_sdl")
    shelltools.cd("..")
    shelltools.copytree("work", "%s/usr/share/abuse_sdl/data" % get.installDIR())
    pisitools.remove("/usr/share/abuse_sdl/data/pisiBuildState")
