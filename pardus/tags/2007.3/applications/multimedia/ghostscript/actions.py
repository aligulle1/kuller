#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.in", "\$\(gsdatadir\)/lib", "/usr/share/ghostscript/8.60/lib")
    pisitools.dosed("Makefile.in", "$(gsdir)/fonts", "/usr/share/fonts/default/ghostscript/")

    shelltools.system("./autogen.sh \
                       --disable-maintainer-mode \
                       --enable-dynamic \
                       --disable-compile-inits \
                       --with-jbig2dec \
                       --with-jasper \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --with-ijs \
                       --with-omni \
                       --with-x \
                       --enable-cups \
                       --with-drivers=ALL,gdi \
                       --with-fontpath=/usr/share/fonts:/usr/share/fonts/default/ghostscript:/usr/share/cups/fonts:/usr/share/fonts/TTF:/usr/share/fonts/Type1 \
                       --disable-gtk")

def build():
    autotools.make("-j1")
    autotools.make("-j1 so")

    shelltools.cd("ijs/")
    shelltools.system("./autogen.sh \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --disable-static \
                       --disable-maintainer-mode \
                       --enable-shared")
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "soinstall")

    pisitools.removeDir("/usr/share/ghostscript/8.60/doc")

    pisitools.dodoc("doc/README", "doc/COPYING", "doc/COPYING.LGPL")
    pisitools.dohtml("doc/")

    # Install ijs
    shelltools.cd("ijs")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # File conflicts with gcc
    pisitools.remove("/usr/share/man/de/man1/ansi2knr.1")
    pisitools.remove("/usr/share/man/man1/ansi2knr.1")
