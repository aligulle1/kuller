#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "squashfs%s" % get.srcVERSION()

def setup():
    pisitools.dosed("squashfs-tools/Makefile", "-O2", "${CFLAGS}")

def build():
    autotools.make('-C squashfs-tools/ CC="%s"' % get.CC())

def install():
    pisitools.dobin("squashfs-tools/mksquashfs")
    pisitools.dobin("squashfs-tools/unsquashfs")

    pisitools.dodoc("CHANGES", "README-4.0", "COPYING", "ACKNOWLEDGEMENTS", "PERFORMANCE*")
