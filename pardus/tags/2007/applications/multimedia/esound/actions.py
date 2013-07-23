#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.automake()
    libtools.libtoolize()
    autotools.configure("--with-libwrap \
                         --enable-alsa \
                         --enable-ipv6 \
                         --sysconfdir=/etc/esd")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "MAINTAINERS", "NEWS", "README", "TIPS", "TODO")
    pisitools.dohtml("docs/html")

