#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def setup():
    shelltools.cd("vnc_unixsrc")
    shelltools.system("xmkmf -a")

    shelltools.cd("Xvnc")
    shelltools.export("IMAKECPP",  "/usr/bin/cpp")
    autotools.rawConfigure()

def build():
    shelltools.cd("vnc_unixsrc")
    autotools.make("World -j1")


    shelltools.cd("Xvnc")
    autotools.make("World -j1")

    shelltools.cd("../..")
    shelltools.cd("vnc_javasrc")
    autotools.make("all")

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/share/man/man1")
    pisitools.dodir("/usr/share/vnc/classes")

    shelltools.cd("vnc_unixsrc")
    shelltools.system("./vncinstall %s/usr/bin %s/usr/share/man" % (get.installDIR(),  get.installDIR()))
    pisitools.dodoc("ChangeLog", "LICENCE.TXT", "README", "WhatsNew")

    shelltools.cd("..")
    shelltools.cd("vnc_javasrc")
    autotools.rawInstall("INSTALL_DIR=%s/usr/share/vnc/classes" % get.installDIR())
