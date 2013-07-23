#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    scons.make("USE_EXT_BOOST=1 PREFIX=/usr DESTDIR=%s" % get.installDIR())

def install():
    insparam = 'PREFIX="/usr" DESTDIR="%s" install' % get.installDIR()
    scons.install(insparam)

    pisitools.dodoc("COPYING", "README")
