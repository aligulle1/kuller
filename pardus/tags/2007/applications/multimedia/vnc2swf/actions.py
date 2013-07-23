#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dosed("Makefile", "mkdir -p $(bindir)", "")
    autotools.install("prefix=%s/usr" % get.installDIR())
    
    pisitools.dodoc("README")
    
    shelltools.cd("docs")
    pisitools.dodoc("*")

