#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-policy-kit \
                         --enable-acpi-ibm \
                         --enable-acpi-toshiba \
                         --with-dell-backlight \
                         --enable-umount-helper \
                         --enable-sonypic \
                         --enable-console-kit \
                         --enable-acl-management \
                         --with-usb-csr \
                         --with-macbook \
                         --with-macbookpro \
                         --with-cpufreq \
                         --with-keymaps \
                         --with-hal-user=hal \
                         --with-hal-group=hal \
                         --with-dbus-sys=/etc/dbus-1/system.d \
                         --disable-docbook-docs \
                         --disable-gtk-doc \
                         --disable-static \
                         --localstatedir=/var \
                         --with-pid-file=/var/run/hald.pid")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # We install this in a seperate package to avoid gnome-python dep
    pisitools.remove("/usr/bin/hal-device-manager")
    pisitools.removeDir("/usr/share/hal/device-manager/")

    # See ya...
    pisitools.removeDir("/etc/hotplug.d/")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README", "HACKING")

    # Needed for hal's new cache infrastructure
    pisitools.dodir("/var/cache/hald/")
