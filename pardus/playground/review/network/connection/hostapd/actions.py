#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def build():
    autotools.make("-C hostapd EXTRA_CFLAGS=\"%s\"" % get.CFLAGS())

def install():
    pisitools.doman("hostapd/hostapd.8")
    pisitools.doman("hostapd/hostapd_cli.1")

    pisitools.dosbin("hostapd/hostapd")
    pisitools.dosbin("hostapd/hostapd_cli")

    pisitools.dodoc("README", "COPYING", "hostapd/wired.conf", "hostapd/hostapd.accept",
                    "hostapd/hostapd.deny", "hostapd/hostapd.eap_user", "hostapd/hostapd.radius_clients",
                    "hostapd/hostapd.vlan", "hostapd/hostapd.wpa_psk")
