#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = get.srcDIR().replace("_", "")

def setup():
    autotools.configure("--with-optim='%s' \
                         --disable-static \
                         --enable-largefile \
                         --enable-shared \
                         --enable-threads \
                         --enable-gl \
                         --enable-xdbe \
                         --enable-xinerama \
                         --enable-xft" % get.CFLAGS())
def build():
    autotools.make()

def check():
    autotools.make("test")

def install():
    autotools.install()
    autotools.rawInstall("DESTDIR=%s -C fluid" % get.installDIR(), "install-linux")

    pisitools.remove("/usr/lib/*.a")
    pisitools.removeDir("/usr/share/man/cat*")

    pisitools.domove("/usr/share/doc/fltk", "%s/%s" % (get.docDIR(), get.srcTAG()), "html")
    pisitools.dodoc("ANNOUNCEMENT", "CHANGES", "COPYING", "CREDITS", "README")
