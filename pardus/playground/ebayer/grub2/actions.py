#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

#WorkDir = ""

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "-Os -g -fno-strict-aliasing")
    shelltools.export("LDFLAGS", "")

    autotools.autoreconf()
    autotools.configure("--libdir=/lib \
                         --datadir=/usr/lib/grub \
                         --exec-prefix=/ \
                         --enable-device-mapper")

def build():
    autotools.make("-j1")

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "BUGS", "COPYING", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
