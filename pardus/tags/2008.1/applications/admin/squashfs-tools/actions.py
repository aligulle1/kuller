#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "squashfs%s/squashfs-tools" % get.srcVERSION()

def setup():
    pisitools.dosed("Makefile", "-O2", "${CFLAGS}")

def build():
    autotools.make('CC="%s"' % get.CC())

def install():
    pisitools.dobin("mksquashfs")
    pisitools.dobin("unsquashfs")

    shelltools.cd("..")
    pisitools.dodoc("README*", "ACKNOWLEDGEMENTS", "CHANGES", "PERFORMANCE.README", "COPYING")

