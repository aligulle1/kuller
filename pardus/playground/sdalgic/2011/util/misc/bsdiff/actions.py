#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile" , ".ifndef WITHOUT_MAN" , "#.ifndef WITHOUT_MAN")
    pisitools.dosed("Makefile" , ".endif" , "#.endif")

def build():
    autotools.make()

def install():
    pisitools.dobin("bsdiff")
    pisitools.dobin("bspatch")

    pisitools.doman("bsdiff.1", "bspatch.1")

