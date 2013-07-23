#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lmpcm_usb-0.5.4"

def build():
    autotools.make()

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "lmpcm_usb.ko")

