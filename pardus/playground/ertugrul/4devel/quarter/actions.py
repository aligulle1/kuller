#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "Quarter-1.0.0"

def setup():
    autotools.configure("--with-x \
                         --with-coin \
                         --with-doxygen \
                         --enable-html \
                         --datadir=/usr/share/doc \
                         --with-qt-designer-plugin-path=/usr/qt/4/plugins/designer")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
