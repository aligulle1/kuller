#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

ZLIBSRC="libs/zlib-1.2.3"
JPEGSRC="libs/jpeg-6b"
# LPNGSRC="libs/libpng-1.2.12"
LPNGSRC="libs/libpng-1.2.8"
# FT2SRC="libs/freetype2-2.2.1"
FT2SRC="libs/freetype-2.1.9"

def exportstuff():
    shelltools.export("ZLIBSRC", ZLIBSRC)
    shelltools.export("LPNGSRC", LPNGSRC)
    shelltools.export("JPEGSRC", JPEGSRC)
    shelltools.export("FT2SRC", FT2SRC)
    shelltools.export("QUIET", "false")

def setup():
    exportstuff()

    # shelltools.echo("config.h", "#undef CONFIG_SILENT_KD_GRAPHICS")
    # shelltools.echo("config.h", "#define CONFIG_PNG 1")
    # shelltools.echo("config.h", "#define CONFIG_TTF 1")
    # shelltools.echo("config.h", "#define CONFIG_TTF_KERNEL 1")

    pisitools.dosed("Makefile", "^CFLAGS[ \t]*=.*", "CFLAGS = %s" % get.CFLAGS())
    pisitools.dosed("splash.h", "#define TTY_SILENT.*", "#define TTY_SILENT 16")

    # There is no -fno-stack-protector on our gcc 3.4.4 :P
    pisitools.dosed("Makefile", "-fno-stack-protector")

    # Make sure zlib makefile is regenerated
    pisitools.remove("%s/Makefile" % ZLIBSRC)

    autotools.rawConfigure("--with-fbsplash \
                         --with-png \
                         --without-mng \
                         --with-ttf \
                         --with-ttfkern")

def build():
    exportstuff()

    autotools.make("-j1 LIB=lib")

def install():
    exportstuff()

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("docs/*", "README", "AUTHORS")

    pisitools.dodir("/lib/splash/tmp")
    pisitools.dodir("/lib/splash/cache")
    pisitools.dodir("/lib/splash/bin")

    pisitools.dosym("/lib/splash/bin/fbres", "/sbin/fbres")
    pisitools.dosym("splash_util", "/sbin/splash_util.static")


