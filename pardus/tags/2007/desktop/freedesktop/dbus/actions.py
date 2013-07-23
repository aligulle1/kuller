#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.autoreconf()
    libtools.libtoolize("--copy --force")

    autotools.configure("--with-x \
        --enable-gtk \
        --enable-python \
        --disable-mono \
        --enable-dnotify \
        --disable-gcj \
        --enable-glib \
        --with-xml=libxml \
        --with-system-pid-file=/var/run/dbus.pid \
        --with-system-socket=/var/run/dbus/system_bus_socket \
        --with-session-socket-dir=/tmp \
        --with-dbus-user=dbus \
        --localstatedir=/var \
        --enable-doxygen-docs \
        --disable-xml-docs \
        --enable-qt3=%s --with-qt3-moc=%s/bin/moc \
        --disable-qt --without-qt-moc" % (get.qtDIR(), get.qtDIR()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # clean pyc/pyo's
    pythonmodules.fixCompiledPy()

    # needs to exist for the system socket
    pisitools.dodir("/var/run/dbus")
    pisitools.dodir("usr/lib/dbus-1.0/services")
    pisitools.dodir("/usr/share/dbus-1/services")

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README", "doc/TODO")
    pisitools.dohtml("doc/")
