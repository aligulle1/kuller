#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-extfs \
                         --enable-hfsp \
                         --enable-fat \
                         --enable-ntfs \
                         --enable-reiserfs=no \
                         --enable-reiser4=no \
                         --enable-xfs=no \
                         --enable-static=no \
                         --enable-ncursesw")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "COPYING", "ChangeLog", "INSTALL", "NEWS", "README", "TODO")
