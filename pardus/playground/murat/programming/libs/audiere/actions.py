#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    libtools.libtoolize("--copy --force")
    autotools.autoconf()

    autotools.configure("--disable-static \
                         --enable-opt")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("doc/*.txt")
