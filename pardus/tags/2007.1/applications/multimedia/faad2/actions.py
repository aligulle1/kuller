#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "faad2"

def setup():
    shelltools.export("WANT_AUTOCONF", "2.5")
    shelltools.export("WANT_AUTOMAKE", "1.7")
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())

    shelltools.system("sh ./bootstrap")
    autotools.configure("--without-xmms \
                        --with-drm")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "README.linux", "TODO")

    pisitools.dosed("%s/usr/include/mp4ff.h" % get.installDIR(), '"mp4ff_int_types.h"', '<stdint.h>')

