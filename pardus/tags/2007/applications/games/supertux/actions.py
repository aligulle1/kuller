#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get 

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --disable-debug \
                         --enable-opengl")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s" \
                         desktopdir=/usr/share/applications \
                         icondir=/usr/share/pixmaps' % get.installDIR())
                       
    pisitools.dodoc("AUTHORS", "ChangeLog", "LEVELDESIGN", "README", "TODO")

    # We will use a modified desktop file, for now
    pisitools.remove("/usr/share/applications/supertux.desktop")
