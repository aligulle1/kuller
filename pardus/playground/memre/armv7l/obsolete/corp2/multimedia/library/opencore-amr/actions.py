#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.environment["CXXFLAGS"] = "%(CXXFLAGS)s -lstdc++" % autotools.environment
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall('PREFIX=/usr \
                          DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog","NEWS", "README","LICENSE")
