#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cache = [ "ac_cv_libiconv_utf8=${ac_cv_libiconv_utf8=yes}",
              "ac_cv_have_abstract_sockets=${ac_cv_have_abstract_sockets=yes}" ]

    pisitools.dosed("dbus/Makefile.in", r"(^program_transform_name\s*=).*$", r"\1")
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
                          --disable-doxygen-docs \
                          --disable-xml-docs", cache=cache)

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README")
