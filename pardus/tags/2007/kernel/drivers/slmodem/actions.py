#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="slmodem-%s" % get.srcVERSION().replace("_", "-")

def setup():
    pisitools.dosed("drivers/Makefile", "SUBDIRS=\$(shell pwd)", "SUBDIRS=%s/drivers" % get.srcDIR())
    pisitools.dosed("drivers/Makefile", "SUBDIRS=", "M=")

def build():
    autotools.make("SUPPORT_ALSA=1 modem")
    autotools.make("KERNEL_DIR=/usr/src/linux drivers")

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "drivers/*.ko")
    pisitools.insinto("/usr/sbin", "modem/modem_test", "slmodem_test")
    pisitools.dosbin("modem/slmodemd")
    pisitools.dodir("/var/lib/slmodem")

    pisitools.dodoc("Changes", "README")

