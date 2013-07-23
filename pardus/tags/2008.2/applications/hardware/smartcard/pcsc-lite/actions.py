#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-usbdropdir=/usr/lib/readers/usb \
                         --enable-muscledropdir=/usr/share/pcsc/services \
                         --enable-runpid=/var/run/pcscd.pid \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "DRIVERS", "HELP", "NEWS")
    pisitools.dodoc("README", "SECURITY", "doc/*.pdf", "doc/README.DAEMON")
