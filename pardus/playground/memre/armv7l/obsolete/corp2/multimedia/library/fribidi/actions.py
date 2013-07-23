#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.environment["CFLAGS"] = "-I%(SysRoot)s/usr/include -march=armv7-a -mtune=cortex-a8 -mfpu=neon -mfloat-abi=softfp -pipe -DPAGE_SIZE=4096" % autotools.environment
    from pisi.actionsapi import shelltools
    shelltools.export("LC_ALL", "C")
    #autotools.environment["CFLAGS"] = "%(CFLAGS)s -DPAGE_SIZE=4096" % autotools.environment
    autotools.configure("--disable-static \
                         --with-pic \
                         --with-gnu-ld")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "NEWS", "README", "ChangeLog", "THANKS", "TODO")
