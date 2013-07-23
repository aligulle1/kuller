#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
#from pisi.actionsapi import get

def setup():
    autotools.aclocal()
    autotools.automake("--add-missing")
    autotools.autoreconf()
    autotools.configure("--prefix=/usr")

def build():
    autotools.make()

def install():
    pisitools.dobin("cmatrix")

    pisitools.doman("cmatrix.1")

    pisitools.insinto("/usr/share/consolefonts", "matrix.psf.gz")
    pisitools.insinto("/usr/share/consolefonts", "mtx.pcf")
    pisitools.insinto("/usr/share/cmatrix", "cmatrix.c")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
