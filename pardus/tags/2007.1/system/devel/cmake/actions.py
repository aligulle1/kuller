#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --system-libs \
                            --docdir=/share/doc/cmake-%s-%s \
                            --mandir=/share/man" % (get.srcVERSION(),get.srcRELEASE()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    pisitools.dosed("%s/usr/share/man/man1/*" % get.installDIR(), "%s" % get.curDIR(), "/usr/share/CMake")
    pisitools.dosed("%s/usr/share/doc/cmake-%s-%s/*" % (get.installDIR(),get.srcVERSION(),get.srcRELEASE()), "%s" % get.curDIR() , "/usr/share/CMake")
