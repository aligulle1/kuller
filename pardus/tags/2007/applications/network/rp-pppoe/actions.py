#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("gui/Makefile.in", "\(@CC@\) \(-o pppoe-wrapper wrapper.o\)", "\1 -Wl,-z,now \2")

    shelltools.cd("src")
    autotools.configure("--enable-plugin=../ppp-2.4.3")

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    shelltools.cd("src")
    autotools.rawInstall("RPM_INSTALL_ROOT=\"%s\" docdir=/usr/share/doc/%s" % (get.installDIR(), get.srcTAG()))

    # Don't use compiled rp-pppoe plugin; use it from the current version of pppd
    pisitools.remove("/etc/ppp/plugins/rp-pppoe.so")
    pisitools.dosym("/usr/lib/pppd/2.4.2/rp-pppoe.so", "/etc/ppp/plugins/rp-pppoe.so")

    # Install symnlinks for easier usage
    pisitools.dosym("/usr/sbin/pppoe-setup","/usr/sbin/adsl-setup")
    pisitools.dosym("/usr/sbin/pppoe-connect","/usr/sbin/adsl-connect")
    pisitools.dosym("/usr/sbin/pppoe-status","/usr/sbin/adsl-status")
    pisitools.dosym("/usr/sbin/pppoe-start","/usr/sbin/adsl-start")
    pisitools.dosym("/usr/sbin/pppoe-stop","/usr/sbin/adsl-stop")
