#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/dee-filter.h", "typedef struct _Dee", "//typedef struct _Dee")
    pisitools.dosed("src/dee-filter-model.h", "typedef struct _Dee", "//typedef struct _Dee")

    autotools.autoreconf("-vfi")
    autotools.configure("--enable-introspection=no")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "TODO")
