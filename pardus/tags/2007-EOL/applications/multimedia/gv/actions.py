#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    for file in ["src/gv_class.ad","src/gv_user.ad","src/gv_system.ad","src/Makefile.am","src/Makefile.in"]:
        pisitools.dosed(file,"-dGraphicsAlphaBits=2","-dAlignToPixels=0")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "README", "TODO")

