#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "pm-utils-0.20.0.20061031"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/etc/pm/hooks/01grub")
    pisitools.remove("/etc/pm/hooks/20video")
    pisitools.remove("/etc/pm/hooks/90clock")

    pisitools.dodoc("README", "COPYING", "ChangeLog", "AUTHORS")
