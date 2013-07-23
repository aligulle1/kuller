#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

BuildNo = get.srcVERSION().split('_')[1]
WorkDir = "NVIDIA-Linux-x86-1.0-%s" % BuildNo
NoStrip = "/"

def build():
    shelltools.export("SYSSRC","/usr/src/linux-%s" % get.curKERNEL())
    shelltools.cd("usr/src/nv")

    autotools.make("module")

def install():
    pisitools.insinto("/lib/modules/%s/kernel/drivers/video" % get.curKERNEL(), "usr/src/nv/nvidia.ko")
