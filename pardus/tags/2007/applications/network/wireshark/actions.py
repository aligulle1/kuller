#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-user-local=no \
                         --with-ssl \
                         --with-plugins=/usr/lib/wireshark/plugins")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps", "image/hi48-app-wireshark.png", "wireshark.png")
    pisitools.insinto("/usr/share/applications/", "wireshark.desktop")

    pisitools.dodoc("AUTHORS", "ChangeLog", "FAQ", "COPYING", "NEWS", "README*")
