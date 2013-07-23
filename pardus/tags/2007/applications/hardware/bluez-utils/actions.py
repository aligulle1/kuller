#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-pie \
                         --enable-alsa \
                         --enable-cups \
                         --enable-dbus \
                         --enable-bccmd \
                         --enable-avctrl \
                         --enable-dfutool \
                         --enable-hid2hci \
                         --enable-obex \
                         --enable-fuse \
                         --disable-initscripts \
                         --localstatedir=/var")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
    pisitools.insinto("/etc/conf.d/", "scripts/bluetooth.default", "bluetooth")

    # optional bluetooth utils
    pisitools.dobin("hcid/passkey-agent")
    pisitools.dosbin("tools/hcisecfilter")
    pisitools.dosbin("tools/ppporc")
