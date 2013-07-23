#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-static=no \
                         --enable-security \
                         --with-x \
                         --with-bluetooth=/usr/lib")

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.insinto("/etc", "Docs/sample/gnokiirc")

    pisitools.dodoc("Docs/*")
    pisitools.doman("Docs/man/*")
