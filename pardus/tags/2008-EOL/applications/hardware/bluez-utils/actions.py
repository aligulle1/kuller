#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())
    shelltools.export("CFLAGS", get.CFLAGS())
    shelltools.export("CXXLAGS", get.CXXFLAGS())

    # Remove shipped glib
    shelltools.system("rm -r %s/eglib/*.[ch]" % get.curDIR())

    autotools.autoreconf("-fi")

    autotools.configure("--enable-glib \
                         --enable-network \
                         --enable-serial \
                         --enable-input \
                         --enable-audio \
                         --enable-gstreamer \
                         --enable-alsa \
                         --enable-usb \
                         --enable-netlink \
                         --enable-tools \
                         --enable-bccmd \
                         --enable-hid2hci \
                         --enable-dfutool \
                         --enable-hidd \
                         --enable-dund \
                         --enable-pand \
                         --enable-cups \
                         --enable-manpages \
                         --enable-configfiles \
                         --enable-test \
                         --disable-initscripts \
                         --disable-pcmciarules \
                         --localstatedir=/var")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C tools/ DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C test/ DESTDIR=%s" % get.installDIR())

    # Replace helper with its full path
    pisitools.dosed("scripts/bluetooth.rules", "RUN\+\=\"bluetooth_serial\"", "RUN+=\"/lib/udev/bluetooth_serial\"")

    # Install udev rule for PCMCIA devices
    pisitools.insinto("/lib/udev/rules.d", "scripts/bluetooth.rules", "70-bluetooth-pcmcia.rules")

    # Install udev script
    pisitools.dobin("scripts/bluetooth_serial", "/lib/udev")

    # Install conf files
    for i in ["audio", "input", "network"]:
        pisitools.insinto("/etc/bluetooth", "%s/%s.conf" % (i,i))

    # Simple test tools
    pisitools.dobin("test/passkey-agent")
    pisitools.dobin("test/auth-agent")
    pisitools.dobin("test/hsmicro")
    pisitools.dobin("test/hsplay")
    pisitools.dobin("test/hstest")
    pisitools.dobin("test/attest")
    pisitools.dobin("test/apitest")
    pisitools.dobin("input/test-input")

    # Additional tools
    pisitools.dosbin("tools/hcisecfilter")
    pisitools.dosbin("tools/ppporc")

    # Install documents
    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
