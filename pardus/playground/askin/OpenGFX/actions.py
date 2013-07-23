#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="opengfx-0.2.4-source"
def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("INSTALL_DIR=%s/usr/share/games/openttd/data" % get.installDIR())
