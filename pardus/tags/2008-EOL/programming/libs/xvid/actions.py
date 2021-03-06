#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "xvidcore-%s/build/generic" % get.srcVERSION()

def setup():
    autotools.autoconf()
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Fixup libs and remove static one
    pisitools.dosym("libxvidcore.so.4.1",  "/usr/lib/libxvidcore.so")
    pisitools.dosym("libxvidcore.so.4.1",  "/usr/lib/libxvidcore.so.4")
    pisitools.remove("/usr/lib/libxvidcore.a")

    shelltools.cd("../..")
    pisitools.insinto("/usr/share/doc/%s/examples" % get.srcTAG(), "examples/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
