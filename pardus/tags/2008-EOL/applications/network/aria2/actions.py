#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls \
                         --disable-rpath \
                         --enable-bittorrent \
                         --enable-metalink \
                         --with-gnutls \
                         --with-sqlite3 \
                         --with-libxml2 \
                         --with-libcares")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
