#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "pidgin-facebookchat"

def build():
    autotools.make("libfacebook.so")

def install():
    #Upstream Makefile is too bad
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dolib("libfacebook.so", "/usr/lib/purple-2")

    for i in("16", "22", "48"):
        pisitools.insinto("/usr/share/pixmaps/pidgin/protocols/%s" %i, "facebook%s.png" %i, "facebook.png")

    pisitools.dodoc("COPYING")
