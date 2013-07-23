#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

def setup():
    shelltools.export("CFLAGS", "%s %s" % (get.CFLAGS(), os.popen("pkg-config --cflags --libs nss").read().strip()))
    shelltools.export("AUTOPOINT", "/bin/true")
    autotools.autoreconf("-fi")
    autotools.configure("--localstatedir=/opt/rpm/var \
                         --bindir=/opt/rpm/bin \
                         --sbindir=/opt/rpm/sbin \
                         --with-external-db \
                         --with-lua \
                         --with-cap \
                         --with-acl \
                         --enable-python \
                         --disable-plugins \
                         --without-selinux")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove symlinks
    pisitools.remove("/opt/rpm/bin/rpmquery")
    pisitools.remove("/opt/rpm/bin/rpmverify")

    # Remove development stuff
    pisitools.removeDir("/usr/include")
    pisitools.removeDir("/usr/lib/pkgconfig")

    pisitools.dodoc("COPYING", "README")
