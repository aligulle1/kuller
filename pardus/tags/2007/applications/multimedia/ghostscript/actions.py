#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "espgs-8.15.1"

def setup():
    pisitools.dosed("Makefile.in", "\$\(gsdatadir\)/lib", "/usr/share/ghostscript/8.15/lib")
    pisitools.dosed("Makefile.in", "$(gsdir)/fonts", "/usr/share/fonts/default/ghostscript/")

    shelltools.system("./autogen.sh \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --with-ijs \
                       --with-omni \
                       --with-x \
                       --enable-cups \
                       --with-drivers=ALL,gdi \
                       --with-fontpath=/usr/share/fonts:/usr/share/fonts/default/ghostscript:/usr/share/fonts/TTF:/usr/share/fonts/Type1")

def build():
    autotools.make("-j1")
    autotools.make("so -j1")

    shelltools.cd("ijs/")
    autotools.configure()
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "soinstall")

    pisitools.removeDir("/usr/share/ghostscript/8.15/doc")

    pisitools.dodoc("doc/README", "doc/COPYING", "doc/COPYING.LGPL")
    pisitools.dohtml("doc/")

    # Install ijs
    shelltools.cd("ijs")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # collision with gcc
    pisitools.remove("/usr/share/man/de/man1/ansi2knr.1")
    pisitools.remove("/usr/share/man/man1/ansi2knr.1")
