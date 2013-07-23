#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-plotutils \
                         --with-ncurses \
                         --enable-nls")

def build():
    autotools.make()
    autotools.make("html")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for f in ["ABOUT-NLS", "AUTHORS", "ChangeLog", "INSTALL", "NEWS", "ONEWS", "README", "THANKS", "TODO"]:
        pisitools.dodoc(f)

    for f in ["ChangeLog", "descript.stat"]:
        pisitools.insinto("%s/%s/examples" % (get.docDIR(), get.srcTAG()), "examples/" + f)

    pisitools.dohtml("doc/pspp.html/*.html")

