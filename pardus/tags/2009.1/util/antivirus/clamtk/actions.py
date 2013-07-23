#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os
import fnmatch
from pisi.actionsapi import pisitools


def setup():
    pisitools.dosed("clamtk", "use ClamTk::App;", "use lib \"/usr/lib/\";\nuse ClamTk::App;")
    pisitools.dosed("clamtk.desktop", "(?<=Name\=).*", "ClamTK")
    pisitools.dosed("clamtk.desktop", "(?<=Name\[tr\]\=).*", "ClamTK")
    pisitools.dosed("clamtk.desktop", "(?<=GenericName\=).*", "Virus Scanner\nGenericName[tr]=Virüs Tarayıcısı")


def install():
    pisitools.dobin("clamtk")
    pisitools.insinto("/usr/lib", "lib", "ClamTk")
    pisitools.doman("clamtk.1.gz")
    pisitools.insinto("/usr/share/applications", "clamtk.desktop")
    pisitools.insinto("/usr/share/pixmaps", "clamtk.png")
    pisitools.dodoc("CHANGES", "DISCLAIMER", "LICENSE", "README")

    #Locales
    for i in os.listdir("po"):
        if fnmatch.fnmatch(i, '*.po'):
            pisitools.domo("po/" + i, i.replace(".po", ""), "clamtk.mo")
