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
                         hotplugdocdir=/usr/share/doc/%s/linux-hotplug \
                         udevscriptdir=/lib/udev"
                         % (get.installDIR(), get.srcTAG(), get.srcTAG(), get.srcTAG()))

    pisitools.removeDir("/usr/share/doc/libgphoto2")
    pisitools.removeDir("/usr/share/doc/libgphoto2_port")

    pisitools.dodoc("ChangeLog", "NEWS*", "README", "AUTHORS", "TESTERS", "MAINTAINERS", "HACKING", "CHANGES")
