#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ntfs-3g-%s" % get.srcVERSION()[4:]

def setup():
    autotools.environment["CFLAGS"] = "%(CFLAGS)s -D_FILE_OFFSET_BITS=64" % autotools.environment
    autotools.configure("--exec-prefix=/ \
                         --bindir=/bin \
                         --sbindir=/sbin \
                         --libdir=/usr/lib \
                         --disable-static \
                         --disable-ldconfig \
                         --with-fuse=external \
                         --docdir=/usr/share/doc/%s" % get.srcNAME())

def build():
    autotools.make()

def install():
    autotools.rawInstall("program_transform_name= DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "CREDITS", "NEWS", "README")
