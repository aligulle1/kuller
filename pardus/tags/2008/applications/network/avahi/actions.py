#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-distro=none \
                         --disable-monodoc \
                         --disable-static \
                         --disable-xmltoman \
                         --disable-mono \
                         --disable-qt3 \
                         --disable-qt4 \
                         --disable-doxygen-doc \
                         --disable-gtk \
                         --disable-pygtk \
                         --disable-glib \
                         --disable-gobject \
                         --enable-autoipd \
                         --enable-core-docs \
                         --enable-python \
                         --enable-python-dbus \
                         --enable-shared \
                         --enable-compat-howl \
                         --enable-compat-libdns_sd \
                         --localstatedir=/var \
                         --with-avahi-user=avahi \
                         --with-avahi-group=avahi \
                         --with-autoipd-user=avahi \
                         --with-autoipd-group=avahi \
                         --with-avahi-priv-access-group=avahi")

def build():
    # for mono sandbox errors
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.make()

def install():
    # for mono sandbox errors
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pythonmodules.fixCompiledPy()

    # Remove unneded files and directory
    pisitools.removeDir("/var")

    # this is from avahi-glib package
    pisitools.remove("/usr/share/avahi/interfaces/avahi-discover.glade")

    pisitools.dosym("/usr/include/avahi-compat-libdns_sd/dns_sd.h", "/usr/include/dns_sd.h")
    pisitools.dodoc("docs/AUTHORS","docs/README","docs/TODO")
