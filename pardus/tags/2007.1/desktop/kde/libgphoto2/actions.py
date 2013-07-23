#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-rpmbuild=/bin/false \
                         --with-drivers=all \
                         --with-exif-prefix=/usr \
                         --enable-nls \
                         --disable-static")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s \
                         gphotodocdir=/usr/share/doc/%s \
                         HTML_DIR=/usr/share/doc/%s/sgml \
                         hotplugdocdir=/usr/share/doc/%s/linux-hotplug" \
                         % (get.installDIR(), get.srcTAG(), get.srcTAG(), get.srcTAG()))

    pisitools.removeDir("/usr/share/doc/libgphoto2")
    pisitools.removeDir("/usr/share/doc/libgphoto2_port")

    pisitools.dodoc("ChangeLog", "NEWS*", "README", "AUTHORS", "TESTERS", "MAINTAINERS", "HACKING", "CHANGES")

    pisitools.dodir("/etc/udev/rules.d/")
    pisitools.dodir("/usr/share/hal/fdi/information/10freedesktop/")

    shelltools.system("%s/usr/lib/libgphoto2/print-udev-rules > %s/etc/udev/rules.d/60-libgphoto2.rules" % (get.installDIR(), get.installDIR()))
    shelltools.system("%s/usr/lib/libgphoto2/print-camera-list hal-fdi > %s/usr/share/hal/fdi/information/10freedesktop/10-camera-libgphoto2.fdi" % (get.installDIR(), get.installDIR()))
    shelltools.system("%s/usr/lib/libgphoto2/print-camera-list hal-fdi-device > %s/usr/share/hal/fdi/information/10freedesktop/10-camera-libgphoto2-device.fdi" % (get.installDIR(), get.installDIR()))
