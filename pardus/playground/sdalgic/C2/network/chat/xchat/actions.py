#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    for f in ["ABOUT-NLS", "NEWS"]:
        shelltools.touch(f)

    autotools.autoreconf("-vfi")
    autotools.configure("--enable-openssl \
                         --enable-ipv6 \
                         --disable-rpath \
                         --enable-threads=posix \
                         --disable-xft \
                         --enable-shm \
                         --disable-textfe \
                         --enable-spell=libsexy")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "HACKING", "README")
