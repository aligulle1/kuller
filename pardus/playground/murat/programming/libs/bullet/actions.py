#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-x \
                         --with-mesa")

def build():
    shelltools.system("jam")

    shelltools.cd("lib")
    autotools.make("shared")

def install():
    shelltools.system("DESTDIR=%s jam install" % get.installDIR())

    pisitools.remove("/usr/lib/*.a")

    pisitools.insinto("/usr/lib", "lib/*so*")

    pisitools.dodoc("AUTHORS", "NEWS", "README", "LICENSE", "VERSION", "*.txt", "*.pdf")
