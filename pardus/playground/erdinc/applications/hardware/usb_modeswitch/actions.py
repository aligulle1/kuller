#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.system("%s %s %s -l usb -o usb_modeswitch usb_modeswitch.c" % (get.CC(), get.CFLAGS(), get.LDFLAGS()))

def install():
    pisitools.dosbin("usb_modeswitch")
    pisitools.insinto("/etc", "usb_modeswitch.conf")
