#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.make("DESTDIR=%s install-djview" % get.installDIR())
    autotools.make("DESTDIR=%s install-nsdejavu" % get.installDIR())

    #Fix plugin path
    shelltools.makedirs("%s/usr/lib/nsbrowser/plugins" % get.installDIR())
    pisitools.domove("/usr/lib/netscape/plugins/nsdejavu.so", "/usr/lib/nsbrowser/plugins")
    pisitools.removeDir("/usr/lib/netscape")

    #Make symbolic link in /opt like all other browser plugins
    pisitools.dosym("/usr/lib/nsbrowser/plugins/nsdejavu.so", "/opt/netscape/plugins/nsdejavu.so")

    #Fix permission
    shelltools.chmod("%s/usr/lib/nsbrowser/plugins/nsdejavu.so" % get.installDIR())

    #Install icon
    pisitools.insinto("/usr/share/pixmaps", "desktopfiles/hi32-djview4.png", "djvulibre-djview4.png")

    #Install desktop file
    pisitools.insinto("/usr/share/applications", "desktopfiles/djvulibre-djview4.desktop")

    pisitools.dodoc("COPYING", "COPYRIGHT", "README*", "TODO")
