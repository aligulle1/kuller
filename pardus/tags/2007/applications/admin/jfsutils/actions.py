#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--sbindir=/sbin --mandir=/usr/share/man/")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/sbin/mkfs.jfs")
    pisitools.dosym("/sbin/jfs_mkfs", "/sbin/mkfs.jfs")
    pisitools.remove("/sbin/fsck.jfs")
    pisitools.dosym("/sbin/jfs_fsck", "/sbin/fsck.jfs")

    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL*", "NEWS", "README*", "COPYING")

