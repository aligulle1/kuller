#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")

    autotools.configure("--with-x \
                         --with-xml=libxml \
                         --with-system-pid-file=/var/run/dbus/pid \
                         --with-system-socket=/var/run/dbus/system_bus_socket \
                         --with-session-socket-dir=/tmp \
                         --with-dbus-user=dbus \
                         --localstatedir=/var \
                         --disable-doxygen-docs \
                         --disable-static \
                         --disable-xml-docs")

def build():
    autotools.make()
    #  Doxygen man page output from 7 to 2 megs
    shelltools.system("./cleanup-man-pages.sh")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # clean pyc/pyo's
    pythonmodules.fixCompiledPy()

    # needs to exist for the system socket
    pisitools.dodir("/var/run/dbus")
    pisitools.dodir("/var/lib/dbus")
    pisitools.dodir("/usr/lib/dbus-1.0/services")
    pisitools.dodir("/usr/share/dbus-1/services")

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README", "doc/TODO")
    pisitools.dohtml("doc/")
