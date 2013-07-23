#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.configure("--enable-mono --enable-ipv6 --enable-largefile --disable-static")

def build():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.make()

def install():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.install()
    pisitools.domove("/usr/bin/uuencode", "/usr/bin", "gmime-uuencode")
    pisitools.domove("/usr/bin/uudecode", "/usr/bin", "gmime-uudecode")
    pisitools.dodoc("ChangeLog", "README*")
    pisitools.domove("/usr/share/gtk-doc/", "/usr/share/doc/%s/html/" % get.srcTAG())
