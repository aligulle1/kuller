#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="prelink-0.0.20071009"

def setup():
    autotools.configure("--enable-static=no")

def build():
    autotools.make()

"""
def check():
    autotools.make("-C testsuite check-harder")
    autotools.make("-C testsuite check-cycle")
"""

def install():
    autotools.install()

    pisitools.rename("/usr/sbin/prelink", "prelink.bin")
    pisitools.dodir("/var/lib/misc")
    pisitools.dodir("/var/log")

    for suffix in ["full", "quick", "force"]:
        shelltools.touch("%s/var/lib/misc/prelink.%s" % (get.installDIR(), suffix))

    shelltools.touch("%s/var/log/prelink.log" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README", "TODO", "THANKS", "AUTHORS", "COPYING", "NEWS")

