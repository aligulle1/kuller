#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libtheora-1.0beta2"

def setup():
    autotools.configure("--enable-shared \
                         --disable-dependency-tracking \
                         --enable-encode \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s" docdir="%s/%s"' % (get.installDIR(), get.docDIR(), get.srcTAG()))

    pisitools.dodoc("README", "AUTHORS", "CHANGES")
