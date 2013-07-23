#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # qemu's configure script did not like other arguments
    autotools.rawConfigure("--prefix=/usr")

    # generated after configure
    pisitools.dosed("qemu/config-host.h",  "CONFIG_QEMU_SHAREDIR \"/usr/share/qemu\"", "CONFIG_QEMU_SHAREDIR \"/usr/share/kvm\"")
    pisitools.dosed("qemu/config-host.mak", "datadir=/usr/share/qemu", "datadir=/usr/share/kvm")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/bin/qemu", "/usr/bin/", "qemu-kvm")
    pisitools.domove("/usr/share/man/man1/qemu.1", "/usr/share/man/man1/", "qemu-kvm.1")

    # Use the one qemu provides
    pisitools.remove("/usr/bin/qemu-img")
    pisitools.remove("/usr/share/man/man1/qemu-img.1")
    pisitools.removeDir("/usr/share/doc")

    # /usr/lib and /usr/include is not needed by KVM
    pisitools.removeDir("/usr/lib")
    pisitools.removeDir("/usr/include")
