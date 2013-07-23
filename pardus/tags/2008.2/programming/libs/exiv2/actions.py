#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.cd("config")
    autotools.autoconf() # buggy mktime() check

    shelltools.move("configure","..")
    shelltools.cd("..")

    autotools.configure("--disable-static")

def build():
    autotools.make()

    shelltools.cd("doc")
    autotools.make()

def install():
    autotools.install()

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("README","doc/ChangeLog")
