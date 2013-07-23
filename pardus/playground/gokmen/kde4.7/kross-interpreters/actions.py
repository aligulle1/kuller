#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde4

shelltools.export("HOME", get.workDIR())

def setup():
    kde4.configure("-DBUILD_csharp=OFF \
                    -DENABLE_KROSSFALCON=OFF \
                    -DENABLE_PHP-QT=ON \
                    -DRUBY_SITE_LIB_DIR=/usr/lib/ruby/site_ruby/1.8 \
                    -DRUBY_SITE_ARCH_DIR=/usr/lib/ruby/site_ruby/1.8/i686-linux")

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dodoc("COPYING")
