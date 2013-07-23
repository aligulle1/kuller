#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "madwifi-ng-r3365-20080226"

def setup():
    for dir in ["ath", "ath_hal", "net80211", "ath_rate/amrr", "ath_rate/onoe", "ath_rate/sample"]:
        pisitools.dosed("%s/Makefile" % dir, "SUBDIRS=", "M=")

    pisitools.dosed("Makefile.inc", "-Werror", "")
    pisitools.dosed("tools/Makefile", "CFLAGS=", "CFLAGS+=")
    pisitools.dosed("tools/Makefile", "LDFLAGS=", "LDFLAGS+=")

def build():
    shelltools.export("KERNELPATH", "/lib/modules/%s/build" % get.curKERNEL())
    shelltools.export("TARGET", "i386-elf")
    shelltools.export("TOOLPREFIX", "/usr/bin/")
    shelltools.export("KERNELRELEASE", get.curKERNEL())
    
    autotools.make("all")

def install():
    autotools.rawInstall("DESTDIR=%s BINDIR=/usr/bin MANDIR=/usr/share/man KMODPATH=/lib/modules/%s/extra" % (get.installDIR(), get.curKERNEL()))
    pisitools.domove("/usr/bin/wlanconfig", "/sbin")

    pisitools.dodoc("README", "COPYRIGHT", "docs/users-guide.pdf", "docs/WEP-HOWTO.txt")

    # install headers for use by wpa_supplicant and hostapd
    pisitools.insinto("/usr/include/madwifi/include/","include/*.h")
    pisitools.insinto("/usr/include/madwifi/net80211", "net80211/*.h")

