#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "blobby_20070115"

def setup():
    shelltools.chmod("bootstrap", 0755)
    shelltools.system("sh ./bootstrap")

    autotools.configure("--with-gamedatadir=/usr/share/blobby")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/applications", "data/blobby.desktop")
    pisitools.insinto("/usr/share/pixmaps", "data/blobby.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README", "TODO", "doc/*.txt")
