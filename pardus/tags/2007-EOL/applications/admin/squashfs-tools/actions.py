#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "squashfs3.1-r2/squashfs-tools"

def setup():
    pisitools.dosed("Makefile", "-O2", "${CFLAGS}")

def build():
    autotools.make('CC="%s"' % get.CC())

def install():
    pisitools.dobin("mksquashfs")
    pisitools.dobin("unsquashfs")
    shelltools.cd("..")
    pisitools.dodoc("README*", "ACKNOWLEDGEMENTS", "CHANGES", "PERFORMANCE.README")

