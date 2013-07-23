#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    # XXX:
    # --enable-tools: Requires if_alg.h user-space crypto API in kernel
    # --enable-nmcompat: nm should be working in order for clients to connect to connman via system bus
    autotools.configure("--enable-gtk-doc \
                         --enable-debug \
                         --enable-pie \
                         --enable-threads \
                         --enable-ethernet \
                         --enable-wifi \
                         --enable-bluetooth \
                         --enable-hh2serial-gps \
                         --enable-ofono \
                         --enable-openconnect \
                         --enable-openvpn \
                         --enable-vpnc \
                         --enable-portal \
                         --enable-loopback \
                         --enable-pacrunner \
                         --enable-google \
                         --enable-iospm \
                         --enable-ntpd \
                         --enable-polkit \
                         --enable-client \
                         --enable-test \
                         --enable-tist \
                         --enable-fake \
                         --enable-capng")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING")
