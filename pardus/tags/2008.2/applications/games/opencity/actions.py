#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "opencity-0.0.6stable"
NoStrip = ["/usr/share/opencity"]

def setup():
    autotools.configure("--disable-sdltest \
                         --enable-sdl-mixer")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/doc")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "COPYRIGHT", "README", "TODO", "docs/FAQ.txt")
