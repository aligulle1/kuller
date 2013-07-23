#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    libtools.libtoolize("--copy --force")
    autotools.aclocal()
    autotools.autoheader()
    autotools.automake("--add-missing --copy")
    autotools.autoconf()

    shelltools.system("glib-gettextize --force --copy")
    shelltools.system("intltoolize --copy --force --automake")

    autotools.configure("--enable-pcmcia-support \
                         --enable-sysfs-carrier \
                         --enable-hotplug-map \
                         --enable-parted \
                         --enable-acpi-acpid \
                         --disable-acpi-proc \
                         --with-hal-user=hal \
                         --with-hal-group=hal \
                         --with-dbus-sys=/etc/dbus-1/system.d \
                         --disable-docbook-docs \
                         --disable-gtk-doc \
                         --enable-doxygen-docs \
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

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "INSTALL", "NEWS", "README")
