#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="jbigkit"

def build():
    autotools.make()

def install():
    pisitools.dobin("pbmtools/jbgtopbm")
    pisitools.dobin("pbmtools/pbmtojbg")

    pisitools.insinto("/usr/include", "libjbig/jbig.h", "jbig.h")

    pisitools.dolib_so("libjbig/libjbig.so")

    pisitools.doman("pbmtools/jbgtopbm.1", "pbmtools/pbmtojbg.1")
    pisitools.dodoc("ANNOUNCE", "CHANGES", "COPYING", "TODO")
