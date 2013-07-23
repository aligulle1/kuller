#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --disable-debug \
                         --disable-rpath \
                         --enable-opengl")

def build():
    shelltools.system("jam")

def install():
    shelltools.system('DESTDIR="%s" jam install' % get.installDIR())

    pisitools.removeDir("/usr/share/doc/supertux2-%s" % get.srcVERSION())
    pisitools.dodoc("WHATSNEW.txt", "README", "COPYING", "docs/levelguidelines.txt")
