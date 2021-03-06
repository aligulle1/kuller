#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.make("-j1")

def install():
    pisitools.insinto("/usr/lib/X11/fonts/xawtv", "*.gz")
    pisitools.insinto("/usr/lib/X11/fonts/xawtv", "fonts.alias")

    shelltools.cd("%s/usr/lib/X11/fonts/xawtv" % get.installDIR())
    shelltools.system("mkfontdir")

