#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    shelltools.system("./autogen.sh")
    autotools.autoreconf()

    autotools.configure("--enable-clients")

def build():
    autotools.make()


def install():
    autotools.install()
    pisitools.domove("/etc/udev/rules.d/70-wayland.rules", "/lib/udev/rules.d")
    pisitools.removeDir("/etc")

    clients = ["dnd", "eventdemo", "flower", "gears", "image", "resizor", "screenshot", "simple-client", "smoke", "terminal"]

    for client in clients:
        pisitools.insinto("/usr/bin/", "clients/%s" % client, "wayland-%s" % client)

