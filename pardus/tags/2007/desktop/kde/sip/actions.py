#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    pythonmodules.run("configure.py \
                       -b /usr/bin \
                       -d /usr/lib/%s/site-packages \
                       -e /usr/include/%s \
                       CFLAGS+=\"%s\" CXXFLAGS+=\"%s\"" % (get.curPYTHON(), get.curPYTHON(), get.CFLAGS(), get.CXXFLAGS()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "LICENSE", "NEWS", "README", "THANKS", "TODO")
    pisitools.dohtml("doc/")
