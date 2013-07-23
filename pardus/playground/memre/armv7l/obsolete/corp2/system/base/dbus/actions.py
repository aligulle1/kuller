#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    crosstools.autoreconf("-fvi")
    crosstools.configure("--with-xml=expat \
                          --with-system-pid-file=/var/run/dbus/pid \
                          --with-system-socket=/var/run/dbus/system_bus_socket \
                          --with-session-socket-dir=/tmp \
                          --with-dbus-user=dbus \
                          --localstatedir=/var \
                          --disable-libaudit \
                          --disable-selinux \
                          --disable-static \
                          --disable-tests \
                          --disable-asserts \
                          --disable-xml-docs \
                          --disable-doxygen-docs \
                          --disable-checks \
                          --disable-tests \
                          --disable-xml-docs \
                          --with-gnu-ld \
                          --x-includes=%(SysRoot)s/usr/include \
                          --x-libraries=%(SysRoot)s/usr/lib \
                          --with-dbus-default-reply-timeout=200000" % crosstools.environment)

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    # clean pyc/pyo's
    pythonmodules.fixCompiledPy()

    # needs to exist for the system socket
    pisitools.dodir("/var/run/dbus")
    pisitools.dodir("/var/lib/dbus")
    pisitools.dodir("/usr/share/dbus-1/services")

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README", "doc/TODO", "doc/*.txt")
    pisitools.dohtml("doc/")
