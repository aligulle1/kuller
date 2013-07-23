#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.autoreconf("-vfi -I ./m4")
    autotools.configure("--disable-static \
                         --enable-ipv6 \
                         --enable-gre \
                         --with-mysql \
                         --with-postgresql")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("COPYING", "LICENSE", "README", "RELEASE.NOTES", "doc/README.database")
    pisitools.dodoc("schemas")

    # Create logdir or barnyard will not start
    pisitools.dodir("/var/log/barnyard2")
