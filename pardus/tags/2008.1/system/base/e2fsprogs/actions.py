#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--enable-elf-shlibs \
                            --disable-e2initrd-helper")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("install install-libs LDCONFIG=/bin/true \
                          DESTDIR=%s root_sbindir=/sbin root_libdir=/lib" % get.installDIR())

    # Unneeded stuff
    pisitools.remove("/usr/lib/*.a")
    pisitools.removeDir("/etc/init.d")

    pisitools.dodoc("ChangeLog", "README", "RELEASE-NOTES")
