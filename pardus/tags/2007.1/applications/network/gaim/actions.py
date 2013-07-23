#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "gaim-2.0.0beta6"

def setup():
    shelltools.move("po/tr.new.po","po/tr.po")
    autotools.configure("--enable-dbus \
                         --disable-gtkspell \
                         --disable-gevolution \
                         --disable-tcl \
                         --disable-tk\
                         --x-includes=/usr/include/X11 \
                         --enable-nss=no \
                         --enable-gnutls=yes \
                         --with-gnutls-includes=/usr/include/gnutls \
                         --with-gnutls-libs=/usr/lib")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    perlmodules.fixLocalPod()
    pisitools.dodoc("AUTHORS", "COPYING", "HACKING", "INSTALL", "NEWS", "PROGRAMMING_NOTES", "README", "ChangeLog")
