#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir = "OpenKinect-libfreenect-bbc109a"
NoStrip = ["/"]

def setup():
    shelltools.export("CFLAGS", "%s -g3 -ggdb" % get.CFLAGS())
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure(sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")

    pisitools.insinto("/etc/udev/rules.d", "platform/linux/udev/*rules")
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("doc/*", "GPL2", "APACHE20", "README*", "HACKING")
