#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    libtools.libtoolize("--force")
    autotools.configure("--enable-shared \
                         --enable-mmx \
                         --disable-gtk \
                         --enable-gpl \
                         --without-cpuflags \
                         --enable-firewire \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.rename("%s/libquicktime" % get.docDIR(), get.srcTAG())
    pisitools.dodoc("README", "TODO", "ChangeLog")
