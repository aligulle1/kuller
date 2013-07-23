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
    shelltools.system("phpize")
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dosed("Makefile", "EXTENSION_DIR = ", "EXTENSION_DIR = %s" % get.installDIR())
    autotools.install()
