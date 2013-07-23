#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "base"
NoStrip = "/"

datadir = "/usr/share/ufoai"

# def setup():
#    shelltools.unlink("game.so")

def install():
    pisitools.dodir(datadir)
    shelltools.cd("..")
    shelltools.copytree("base", "%s/%s/" % (get.installDIR(), datadir))

