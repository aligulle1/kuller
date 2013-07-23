#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.aclocal()
    autotools.autoconf()
    autotools.automake()
    libtools.libtoolize("--copy --force")

    autotools.configure("--enable-largefile \
                         --enable-glib2 \
                         --enable-gconf \
                         --enable-oss \
                         --enable-alsa \
                         --enable-avahi \
                         --enable-bluez \
                         --enable-hal \
                         --enable-tcpwrap \
                         --enable-jack \
                         --enable-lirc \
                         --with-caps \
                         --with-x \
                         --disable-asyncns \
                         --disable-solaris \
                         --disable-ltdl-install \
                         --disable-static \
                         --disable-rpath \
                         --localstatedir=/var \
                         --with-system-user=pulse \
                         --with-system-group=pulse \
                         --with-realtime-group=pulse-rt \
                         --with-access-group=pulse-access")

def build():
    autotools.make()

    #generate html docs 
    autotools.make("doxygen")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README")
    pisitools.dohtml("doxygen/html")

    #needs for service.py
    pisitools.dodir("/var/run/pulse")
