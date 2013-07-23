#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "supertuxkart-%s" % get.srcVERSION()

def removegames(dest):
    for root, dirs, files in os.walk(dest):
        for name in files:
            if name.startswith("Makefile"):
                pisitools.dosed(os.path.join(root, name), "games/")

def setup():
    removegames("./")
    autotools.configure()

def build():
    autotools.make("SUPERTUXKART_DATADIR=/usr/share/supertuxkart")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")

