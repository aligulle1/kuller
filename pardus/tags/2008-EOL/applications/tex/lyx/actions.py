# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-qt-dir=/usr/qt/4 \
                         --with-x \
                         --with-aspell \
                         --with-aiksaurus \
                         --enable-shared=yes \
                         --enable-static=no \
                         --enable-build-type=release \
                         --without-included-boost \
                         --disable-stdlib-debug \
                         --disable-rpath")

def build():
    autotools.make("CXX=%s" % get.CXX())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps/", "lib/images/lyx.png")

    #pisitools.dodoc("ANNOUNCE", "RELEASE-NOTES", "README", "ChangeLog", "NEWS", "COPYING", "ANNOUNCE")
    pisitools.dodoc("ANNOUNCE", "RELEASE-NOTES", "README", "NEWS", "COPYING", "ANNOUNCE")
