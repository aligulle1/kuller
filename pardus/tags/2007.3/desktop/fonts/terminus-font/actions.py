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
    autotools.rawConfigure("--prefix=/usr \
                            --x11dir=/usr/share/fonts/terminus")

def build():
    autotools.make()

def install():
    autotools.make("DESTDIR=%s install" % get.installDIR())
    autotools.make("DESTDIR=%s fontdir" % get.installDIR())

    pisitools.dodoc("README")
