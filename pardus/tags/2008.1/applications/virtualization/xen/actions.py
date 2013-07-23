#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

NoStrip = "/"

def setup():
    shelltools.export("LDFLAGS", "")

    shelltools.cd("tools/ioemu")
    autotools.configure("--enable-sdl \
                         --enable-alsa")

def build():
    shelltools.cd("xen/")
    autotools.make()

    shelltools.cd("../tools/")
    autotools.make("-j1")

    shelltools.cd("firmware/")
    autotools.make()

    shelltools.cd("../../docs/")
    autotools.make()

def install():
    shelltools.cd("xen/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../tools/")
    autotools.rawInstall("DESTDIR=%s XEN_PYTHON_NATIVE_INSTALL=1" % get.installDIR())

    shelltools.cd("firmware/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../../docs/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # clean pyc/o's
    pythonmodules.fixCompiledPy()

    # remove redhat specific dirs
    pisitools.removeDir("/etc/sysconfig")

    # remove unneeded dirs
    pisitools.removeDir("/etc/init.d")
    pisitools.removeDir("/etc/udev")
    pisitools.removeDir("/etc/hotplug")

    # Just pdf ones
    pisitools.removeDir("/usr/share/doc/xen/ps/")

    # xend expects these to exist
    pisitools.dodir("/var/log/xen/console")
    pisitools.dodir("/var/run/xenstored")
    pisitools.dodir("/var/lib/xenstored")
    pisitools.dodir("/var/xen/dump")

    # conflicting with qemu
    pisitools.remove("/usr/share/man/man1/qemu-img.1");
    pisitools.remove("/usr/share/man/man1/qemu.1");

    pisitools.removeDir("/usr/share/doc/qemu/")
