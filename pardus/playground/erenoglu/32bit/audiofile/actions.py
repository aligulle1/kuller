#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("test/Makefile.am", "noinst_PROGRAMS", "check_PROGRAMS")
    autotools.autoreconf("-vfi")

    options = "--disable-static \
               --disable-dependency-tracking \
               --enable-largefile"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":
	#install the libraries
        pisitools.insinto("/usr/lib32","libaudiofile/.libs/libaudiofile.so.0.0.2")
        #do the symlinks
        pisitools.dosym("libaudiofile.so.0.0.2","/usr/lib32/libaudiofile.so")
        pisitools.dosym("libaudiofile.so.0.0.2","/usr/lib32/libaudiofile.so.0")
        #make the pkgconfig dir
        pisitools.dodir("/usr/lib32/pkgconfig")
        pisitools.insinto("/usr/lib32/pkgconfig","audiofile.pc")
    else:
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())

        pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO", "NEWS")
