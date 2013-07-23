#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sysprof"

def setup():
    autotools.aclocal()
    autotools.autoheader()
    autotools.automake("--add-missing")
    autotools.autoconf()

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.doexe("module/sysprof-module.ko", "/lib/modules/%s/extra/" % get.curKERNEL())
