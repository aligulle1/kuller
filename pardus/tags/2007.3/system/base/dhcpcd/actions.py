#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/dhcpconfig.c", "/etc/ntp\.drift", "/var/lib/ntp/ntp.drift")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install("sbindir=%s/sbin" % get.installDIR())
    pisitools.removeDir("/etc/dhcpc")

    pisitools.dodoc ("AUTHORS", "ChangeLog", "NEWS", "README")
