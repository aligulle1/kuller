#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "vnc_unixsrc"

def setup():
    shelltools.system("xmkmf -a")

    shelltools.cd("Xvnc")
    shelltools.export("IMAKECPP", "/usr/bin/cpp")
    autotools.rawConfigure()

def build():
    autotools.make()
    shelltools.cd("Xvnc")
    autotools.make("EXTRA_LIBRARIES=\"-lwrap -lnss_nis\" EXTRA_DEFINES=\"-DUSE_LIBWRAP=1\"")

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/share/man/man1")

    shelltools.system("./vncinstall %s/usr/bin %s/usr/share/man" % (get.installDIR(), get.installDIR()))

    pisitools.insinto("/usr/share/tightvnc/classes", "classes/*")
