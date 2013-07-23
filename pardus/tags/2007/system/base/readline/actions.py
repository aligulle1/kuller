#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-curses --libdir=/usr/lib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    pisitools.domove("/usr/lib/*.so*", "/lib")
    shelltools.chmod("%s/lib/*.so*" % get.installDIR())

    pisitools.dosym("/lib/libreadline.so.5", "/usr/lib/libreadline.so")
    pisitools.dosym("/lib/libhistory.so.5", "/usr/lib/libhistory.so")

    pisitools.dodoc("CHANGELOG", "CHANGES", "README", "USAGE", "NEWS", "doc/*.ps")
    pisitools.dohtml("doc/")
