#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-rpath \
                         --with-enable-www=1 \
                         --with-enable-zoom=1 \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # man is not compressed correctly, adding manually for now
    # Strange handling of man
    # shelltools.system("gunzip xmoto.6.gz")

    pisitools.removeDir("/usr/share/man")
    # pisitools.doman("xmoto.6")

