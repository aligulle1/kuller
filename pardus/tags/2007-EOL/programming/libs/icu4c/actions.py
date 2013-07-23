#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="icu/source"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.move("%s/usr/sbin/*" % get.installDIR(),"%s/usr/bin" % get.installDIR())
    pisitools.removeDir("/usr/sbin")

    pisitools.dosed("%s/usr/bin/icu-config" % get.installDIR(),"-Wl,-Bdirect -Wl,-hashvals -Wl,-zdynsort ","");
