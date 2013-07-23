#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    autotools.autoreconf("-vfi")
    pisitools.dosed("configure","clutter-gtk-0.10","clutter-gtk-0.12")
    autotools.configure("--disable-dependency-tracking \
                         --enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for i in shelltools.ls("examples/events"):
        if i.endswith(".h") or i.endswith(".cc"):
            pisitools.insinto("/%s/%s/examples/" % (get.docDIR(), get.srcNAME()), "examples/events/%s" % i)

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS", "examples/redhand.png")
