#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-kmodule=/usr/src/linux \
                         --with-libusb=/usr \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/lib/modules/%s/kernel/drivers/usb" % get.curKERNEL(), "kbuild/*.ko")

