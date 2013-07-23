#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("WANT_AUTOMAKE", "1.9")
    shelltools.export("WANT_AUTOCONF", "2.5")

    autotools.autoreconf("-fi")

    autotools.configure("--enable-shared \
                         --disable-static \
                         --enable-djbfft")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\" docdir=/usr/share/doc/%s/html" % (get.installDIR(), get.srcTAG()))

    pisitools.dodoc("AUTHORS", "ChangeLog", "HISTORY", "NEWS", "README", "TODO", "doc/liba52.txt")
