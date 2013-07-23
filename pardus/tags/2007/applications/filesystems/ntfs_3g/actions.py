#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="ntfs-3g-0.20061212-BETA"

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    # Let mount -t ntfs-3g , work
    pisitools.dosym("/usr/bin/ntfs-3g", "/sbin/mount.ntfs-3g")
