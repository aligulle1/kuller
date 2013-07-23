#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/Makefile.in", "-O2", get.CFLAGS())
    pisitools.dosed("src/Makefile.in", "install -s", "install")

    autotools.rawConfigure("--prefix=/usr \
                            --mandir=/usr/share/man \
                            --datadir=/usr/share")

def build():
    autotools.make("CC=%s -j1" % get.CC())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/bin/setfont", "/bin")
    pisitools.dosym("/bin/setfont", "/usr/bin/setfont")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("CHANGES", "CREDITS", "README")
