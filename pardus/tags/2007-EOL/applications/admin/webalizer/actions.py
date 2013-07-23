#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="webalizer-2.01-10"

def setup():
    autotools.autoreconf()
    autotools.configure("--enable-dns \
                         --with-language=turkish \
                         --with-dblib=/usr/lib/libdb.so \
                         --enable-geoip")
def build():
    autotools.make()

def install():
    pisitools.dobin("webalizer")
    pisitools.dosym("/usr/bin/webalizer","/usr/bin/webazolver")

    pisitools.doman("webalizer.1")
    pisitools.dodoc("*README*","CHANGES","Copyright")
