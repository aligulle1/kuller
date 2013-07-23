#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "x2x-1.30-beta"

def build():
    shelltools.system("xmkmf -a")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
