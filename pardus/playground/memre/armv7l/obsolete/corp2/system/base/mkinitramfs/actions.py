#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "busybox-%s" % get.srcVERSION()

def build():
    crosstools.make("CROSS_COMPILE=%(target)s-" % crosstools.environment)
    crosstools.make("CROSS_COMPILE=%(target)s- busybox.links" % crosstools.environment)

def install():
    pisitools.insinto("/lib/initramfs", "busybox.links")
    pisitools.insinto("/lib/initramfs", "busybox")

    pisitools.dodir("/etc/initramfs.d")
