#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("makefile", "_pardus_cflags", get.CFLAGS())
    pisitools.dosed("makefile", "_pardus_ldflags", get.LDFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dobin("tomatoes")
    pisitools.insinto("/usr/share/pixmaps", "icon.png", "tomatoes.png")

