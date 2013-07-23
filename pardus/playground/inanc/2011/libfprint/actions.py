#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools

def setup():
    libtools.libtoolize("--copy --force")
    autotools.aclocal()
    autotools.autoheader()
    autotools.autoconf()
    autotools.automake("-ac")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodir("/lib/udev/rules.d")
    pisitools.domove("/etc/udev/rules.d/*.rules", "/lib/udev/rules.d")
    pisitools.removeDir("/etc")

    pisitools.dodoc("AUTHORS", "COPYING", "HACKING", "NEWS", "README", "THANKS", "TODO")
