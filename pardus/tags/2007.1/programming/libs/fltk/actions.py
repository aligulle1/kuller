#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-threads \
                         --enable-xft \
                         --enable-shared")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/lib/*.a")
    pisitools.dosed("%s/usr/bin/fltk-config" % get.installDIR(), "-Wl,-Bdirect -Wl,-hashvals -Wl,-zdynsort", "")
    pisitools.dosed("%s/usr/bin/fltk-config" % get.installDIR(), "libfltk.a", "libfltk.so")
