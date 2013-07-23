#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde

def setup():
    autotools.autoconf()
    pisitools.dosed("kdebluetooth/kbluetoothd/kcm_btpaired/pairedtab.cpp", "/etc/init\.d/bluez-utils", "service bluez-utils")
    kde.configure("--without-xmms \
                   --enable-irmcsynckonnector")

def build():
    kde.make()

def install():
    kde.install()
    pisitools.remove("/usr/kde/3.5/share/autostart/kbluetoothd.autostart.desktop")
