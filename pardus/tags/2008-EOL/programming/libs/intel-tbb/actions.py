#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="tbb21_20080605oss"

def build():
    autotools.make("tbb tbbmalloc")

def install():
    pisitools.dolib("build/linux*release/lib*.so")

    shelltools.chmod("include/tbb/*", 0644)
    shelltools.chmod("include/tbb/machine/*", 0644)
    pisitools.insinto("/usr/include","include/tbb")

    pisitools.dodoc("README","COPYING")
