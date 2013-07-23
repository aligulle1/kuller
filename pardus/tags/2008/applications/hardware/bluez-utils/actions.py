#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-all \
                         --enable-pie \
                         --disable-initscripts \
                         --disable-sdpd \
                         --disable-hidd \
                         --localstatedir=/var")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # move bluetooth rules into correct place
    pisitools.domove("/etc/udev/bluetooth.rules", "/etc/udev/rules.d", "40-bluetooth.rules")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README")

    # optional bluetooth utils
    pisitools.dobin("daemon/passkey-agent")
    pisitools.dobin("daemon/auth-agent")
    pisitools.dosbin("tools/hcisecfilter")
    pisitools.dosbin("tools/ppporc")

    # bluez test
    pisitools.dobin("test/hsmicro")
    pisitools.dobin("test/hsplay")
    pisitools.dobin("test/hstest")
    pisitools.dobin("test/attest")
    pisitools.dobin("test/apitest")
