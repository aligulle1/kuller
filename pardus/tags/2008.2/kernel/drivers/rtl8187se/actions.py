#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "rtl8187se-linux-2.6-1023-1118-2008"

def build():
    pisitools.dosed("Makefile", "^KVER .*$", "KVER = %s" % get.curKERNEL())
    autotools.make()

def install():
    pisitools.insinto("/lib/modules/%s/extra/" % get.curKERNEL(), "ieee80211/ieee80211_crypt_wep-rtl.ko")
    pisitools.insinto("/lib/modules/%s/extra/" % get.curKERNEL(), "ieee80211/ieee80211_crypt_tkip-rtl.ko")
    pisitools.insinto("/lib/modules/%s/extra/" % get.curKERNEL(), "ieee80211/ieee80211_crypt-rtl.ko")
    pisitools.insinto("/lib/modules/%s/extra/" % get.curKERNEL(), "ieee80211/ieee80211_crypt_ccmp-rtl.ko")
    pisitools.insinto("/lib/modules/%s/extra/" % get.curKERNEL(), "ieee80211/ieee80211-rtl.ko")
    pisitools.insinto("/lib/modules/%s/extra/" % get.curKERNEL(), "rtl8185/rtl8187se.ko")

    pisitools.dodoc("README", "ChangeLog", "debug_notes")
