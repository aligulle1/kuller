#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--without-capi \
                         --with-curses \
                         --without-esd \
                         --with-opengl")

def build():
    autotools.make("depend")
    autotools.make()

def install():
    autotools.install()

    pisitools.dosym("/etc/xdg/menus/applications-merged/wine.menu", "/usr/kde/3.5/etc/xdg/menus/applications-merged/wine.menu")

    pisitools.dodoc("ANNOUNCE", "AUTHORS", "COPYING.LIB", "LICENSE*", "README", "documentation/README.*")
