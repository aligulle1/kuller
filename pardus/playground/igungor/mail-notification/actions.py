#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    CONSTS = {"CC" : get.CC(),
              "CFLAGS" : get.CFLAGS(),
              "CXXFLAGS" : get.CXXFLAGS(),
              "LDFLAGS" : get.LDFLAGS(),
              "DESTDIR" : get.installDIR()}

    shelltools.system('./jb configure \
                            cc="%(CC)s" \
                            cflags="%(CFLAGS)s" \
                            cppflags="%(CXXFLAGS)s" \
                            ldflags="%(LDFLAGS)s" \
                            install-gconf-schemas=no \
                            prefix="/usr" \
                            sysconfdir="/etc" \
                            localstatedir="/var" \
                            libdir="/usr/lib" \
                            scrollkeeper-dir="/var/lib/scrollkeeper" \
                            destdir="%(DESTDIR)s"' % CONSTS)

def build():
    shelltools.system('./jb build')

def install():
    shelltools.system('GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1" ./jb install')

    pisitools.dodoc("AUTHORS", "COPYING", "TRANSLATING", "NEWS", "README")

    #pisitools.removeDir("/var/lib/scrollkeeper")
