#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "x2x-1.30-beta"

def build():
    shelltools.system("xmkmf -a")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
