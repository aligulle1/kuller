#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "NVIDIA-Linux-x86-%s" % get.srcVERSION()
NoStrip = "/"

def build():
    shelltools.export("IGNORE_XEN_PRESENCE", "1")

    shelltools.export("SYSSRC","/usr/src/linux-%s/" % get.curKERNEL())
    shelltools.cd("usr/src/nv")

    autotools.make("module")

def install():
    pisitools.insinto("/lib/modules/%s/kernel/drivers/video" % get.curKERNEL(), "usr/src/nv/nvidia.ko")
