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

WorkDir = "ppracer-0.5alpha"

def setup():
    autotools.autoconf()
    autotools.configure("--disable-dependency-tracking \
                         --with-data-dir=/usr/share/ppracer \
                         --with-tcl=/usr/lib \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog")

    pisitools.remove("/usr/share/applications/ppracer.desktop")

