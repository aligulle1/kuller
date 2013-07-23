#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="xf86-video-omapfb-master"

def setup():
    pisitools.dosed("configure.ac", r"(^XORG_DRIVER_CHECK_EXT.*)", "#\\1")
    pisitools.dosed("src/omapfb-xv.c", "fb1", "fb2")

    autotools.environment["CFLAGS"] = "%(CFLAGS)s -I%(SysRoot)s/usr/include/xorg" % autotools.environment

    autotools.autoreconf("-fvi")
    autotools.configure("--enable-neon")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
