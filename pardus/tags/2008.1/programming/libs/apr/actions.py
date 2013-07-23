#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./buildconf")

    # Forcibly prevent detection of shm_open (which then picks up but
    # does not use -lrt).
    shelltools.export("ac_cv_search_shm_open","no")

    autotools.configure("--enable-ipv6 \
                         --enable-threads \
                         --with-installbuilddir=/usr/share/apr/build \
                         --with-devrandom=/dev/urandom \
                         --disable-static")
def build():
    autotools.make()

def check():
    autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosed("%s/usr/bin/apr-1-config" % get.installDIR(), get.workDIR(), "/usr/share/apr")

    pisitools.dodoc("CHANGES", "LICENSE", "NOTICE")
