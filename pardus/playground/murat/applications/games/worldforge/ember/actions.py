#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static \
                         --disable-static-build \
                         --disable-sdltest")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.domove("/usr/share/icons/worldforge/ember.png", "/usr/share/pixmaps")

    pisitools.removeDir("/usr/share/ember/media/user")
    pisitools.removeDir("/usr/share/ember/media/shared/packs")
    pisitools.removeDir("/usr/share/icons")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
