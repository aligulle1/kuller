#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "xen-3.0.3_0-src"
NoStrip = "/"

def build():
    # disable -Bdirect
    shelltools.export("LDFLAGS", "")

    shelltools.cd("xen/")
    autotools.make()

def install():
    shelltools.cd("xen/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
