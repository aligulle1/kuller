#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

WorkDir = "yafray"

def setup():
    pisitools.dosed("*-settings.py", "-O3", "%s -fsigned-char" % get.CXXFLAGS())

def build():
    scons.make("prefix='/usr'")

def install():
    insparam = 'prefix="/usr" destdir="%s" libdir="/lib" install' % get.installDIR()
    scons.install(insparam)

    pisitools.dodoc("AUTHORS")
    pisitools.dohtml("doc/doc.html")
