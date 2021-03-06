#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip=["/usr/share/kvm"]

def setup():
    pisitools.dosed("qemu/configure", "datasuffix=\"/share/qemu\"", "datasuffix=\"/share/kvm\"")

    # qemu's configure script did not like other arguments
    autotools.rawConfigure("--prefix=/usr \
                            --disable-gcc-check")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/bin/qemu-system-x86_64", "/usr/bin/", "qemu-kvm")
    pisitools.domove("/usr/share/man/man1/qemu.1", "/usr/share/man/man1/", "qemu-kvm.1")

    # Use the one qemu provides
    pisitools.remove("/usr/bin/qemu-img")
    pisitools.remove("/usr/share/man/man1/qemu-img.1")
    pisitools.removeDir("/usr/share/doc")

    # /usr/lib and /usr/include is not needed by KVM
    pisitools.removeDir("/usr/lib")
    pisitools.removeDir("/usr/include")
