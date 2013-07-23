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


def setup():
    shelltools.export("CXXFLAGS", "%s -fPIC" % get.CFLAGS())
    autotools.configure()

def build():
    shelltools.export("CXXFLAGS", "%s -fPIC" % get.CFLAGS())
    autotools.make()

def install():
    shelltools.export("CXXFLAGS", "%s -fPIC" % get.CFLAGS())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "KNOWN_BUGS", "NOTICE", "README*", "TODO*")
