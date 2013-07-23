#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "gtk-qt-engine"

def setup():
    shelltools.export("CMAKE_INSTALL_PREFIX", "/usr")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    # Cmake po stuff is broken ATM
    pisitools.domo("po/tr.po", "tr", "gtkqtengine.mo")
    pisitools.domo("po/de.po", "de", "gtkqtengine.mo")
    pisitools.domo("po/es.po", "es", "gtkqtengine.mo")

    # tasma has that
    pisitools.remove("/usr/share/applications/kcmgtk.desktop")
