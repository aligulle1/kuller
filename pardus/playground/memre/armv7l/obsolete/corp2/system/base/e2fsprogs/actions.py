#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("LC_ALL", "C")

    crosstools.autoreconf("-fvi")
    crosstools.rawConfigure("--enable-elf-shlibs \
                             --disable-e2initrd-helper \
                             --disable-libblkid \
                             --disable-libuuid \
                             --disable-uuidd")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("install install-libs LDCONFIG=/bin/true \
                           DESTDIR=%s root_sbindir=/sbin root_libdir=/lib" % get.installDIR())

    # absolute path problem fix.
    for file in ("com_err", "e2p", "ext2fs", "ss"):
        pisitools.remove("/usr/lib/lib%s.so" % file)
        pisitools.dosym("lib%s.so.2" % file, "/lib/lib%s.so" % file)
        pisitools.dosym("../../lib/lib%s.so.2" % file, "/usr/lib/lib%s.so" % file)

    # Unneeded stuff
    pisitools.remove("/usr/lib/*.a")
    pisitools.dodoc("README", "RELEASE-NOTES")
