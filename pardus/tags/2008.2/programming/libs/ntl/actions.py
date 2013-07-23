#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ntl-%s/src" % get.srcVERSION()

def setup():
    autotools.rawConfigure("PREFIX=/usr")

def build():
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                          DOCDIR=/usr/share/doc/%s"
                          % (get.installDIR(), get.srcTAG()))

    pisitools.dodoc("../README")
