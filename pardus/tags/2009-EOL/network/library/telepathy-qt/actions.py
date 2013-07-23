#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "telepathy-qt4-%s" % get.srcVERSION()

QTDIR = {"qt": get.qtDIR()}

def setup():
    autotools.autoreconf("-vfi")
    autotools.rawConfigure("--prefix=%(qt)s \
                            --includedir=%(qt)s/include \
                            --libdir=%(qt)s/lib \
                            --disable-static" % QTDIR )

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
