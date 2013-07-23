#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --includedir=%s/usr/include/xmlrpc-epi" % get.installDIR())

    pisitools.dosed("src/Makefile","libxmlrpc","libxmlrpc-epi")
    pisitools.dosed("sample/Makefile","libxmlrpc","libxmlrpc-epi")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.removeDir("/usr/bin")
