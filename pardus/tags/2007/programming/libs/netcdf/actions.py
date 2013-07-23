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


def setup():
    shelltools.cd("src/")
    shelltools.export("CPPFLAGS", "-Df2cFortran")
    shelltools.export("LD_LIBRARY_PATH", "/usr/lib/gcc/i686-pc-linux-gnu/")
    shelltools.export("FCFLAGS", "-L/usr/lib/gcc/i686-pc-linux-gnu/")
    autotools.configure()

def build():
    shelltools.cd("src/")
    autotools.make()

def install():
    shelltools.cd("src/")
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/share/man/man3/")
    autotools.install("MANDIR=%s/usr/share/man" % (get.installDIR()))
    pisitools.dodoc("COMPATIBILITY", "COPYRIGHT", "MANIFEST", "README")
    pisitools.dohtml(".")
