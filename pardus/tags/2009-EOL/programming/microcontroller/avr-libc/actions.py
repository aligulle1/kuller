#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = "/"

def setup():
    # Force cross compile to avr target
    shelltools.export("CC", "avr-gcc")
    shelltools.export("PATH", "%s:/opt/avr/bin" % get.ENV("PATH"))
    shelltools.system("./configure --prefix=/opt/avr --build=%s --host=avr" % get.HOST())

def build():
    shelltools.export("PATH", "%s:/opt/avr/bin" % get.ENV("PATH"))
    autotools.make()

def install():
    shelltools.export("PATH", "%s:/opt/avr/bin" % get.ENV("PATH"))
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
