#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-glout \
                         --enable-master \
                         --enable-main \
                         --disable-music \
                         --with-x \
                         --disable-useradd \
                         --disable-etc \
                         --disable-initscripts \
                         --disable-sysinstall \
                         --disable-games")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/share/doc/armagetronad/", "/usr/share/doc/%s" % get.srcTAG())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")

    # We better cleanup
    pisitools.remove("/usr/bin/armagetronad-uninstall")
    pisitools.removeDir("/usr/share/armagetronad/desktop")
    pisitools.removeDir("/usr/share/applnk")
    pisitools.removeDir("/usr/share/icons")
    pisitools.removeDir("/etc/init.d")
    shelltools.chmod("%s/etc/armagetronad/rc.config", 0644)
