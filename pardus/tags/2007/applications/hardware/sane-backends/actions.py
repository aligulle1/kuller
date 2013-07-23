#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Those are in gentoo ebuild too, but what are they for?
    # I couldn't find in docs, some comment would be helpful here -gurer
    shelltools.export("SANEI_JPEG", "sanei_jpeg.o")
    shelltools.export("SANEI_JPEG_LO", "sanei_jpeg.lo")

    autotools.configure("--enable-ipv6 \
                         --enable-libusb \
                         --with-gphoto2")

def build():
    autotools.make()

def install():
    autotools.install("docdir=%s/usr/share/doc/%s" % (get.installDIR(), get.srcTAG()))
    pisitools.dodir("/var/lib/lock/sane")

    shelltools.echo("%s/etc/sane.d/dll.conf" % get.installDIR(), "\n# Added for hplip backends\nhpaio\n")

