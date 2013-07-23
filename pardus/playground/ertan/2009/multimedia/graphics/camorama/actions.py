#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-schemas-install")

def build():
    autotools.make()

def install():
    shelltools.export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "1")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 
