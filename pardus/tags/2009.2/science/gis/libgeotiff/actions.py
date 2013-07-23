#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --with-jpeg \
                         --with-libtiff \
                         --with-proj \
                         --with-zip")

def build():
    autotools.make("-j1")
    shelltools.cd("docs")
    shelltools.system("doxygen index.dox")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("bin/makegeo")

    pisitools.remove("/usr/lib/libgeotiff.a")

    pisitools.insinto("/usr/share/epsg_csv", "docs/html")
    pisitools.insinto("/usr/share/epsg_csv", "docs/*.txt")
    pisitools.insinto("/usr/share/epsg_csv", "docs/*.html")

    pisitools.dodoc("README", "LICENSE")
