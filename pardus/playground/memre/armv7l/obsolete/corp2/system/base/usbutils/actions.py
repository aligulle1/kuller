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
    crosstools.configure("--datadir=/usr/share/misc \
                          --disable-zlib")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/sbin/update-usbids.sh")
    pisitools.dodir("/usr/share/pkgconfig")
    pisitools.domove("/usr/share/misc/pkgconfig/*.pc", "/usr/share/pkgconfig/")
    pisitools.removeDir("/usr/share/misc/pkgconfig")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
