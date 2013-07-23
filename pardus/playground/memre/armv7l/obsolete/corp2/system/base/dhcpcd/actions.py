#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    crosstools.configure("--libexecdir=/lib/dhcpcd \
                          --dbdir=/var/lib/dhcpcd \
                          --sbindir=/sbin \
                          --localstatedir=/var")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DBDIR=/var/lib/dhcpcd LIBEXECDIR=/lib/dhcpcd DESTDIR=%s" % get.installDIR())

    # Remove hooks install the compat one
    pisitools.remove("/lib/dhcpcd/dhcpcd-hooks/*")
    pisitools.insinto("/lib/dhcpcd/dhcpcd-hooks", "dhcpcd-hooks/50-dhcpcd-compat")

    pisitools.dodoc("README")
