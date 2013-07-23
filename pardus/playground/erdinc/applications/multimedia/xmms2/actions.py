#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "xmms2-0.4DrKosmos"

def setup():
    shelltools.system("./waf --prefix=/usr/ --with-libdir=/usr/lib \
                      --without-optionals=et configure")

def build():
    shelltools.system("./waf build")

def install():
    shelltools.system("./waf --destdir=%s install" % get.installDIR())
