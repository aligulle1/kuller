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

    # install headers
    pisitools.insinto("/usr/include", "include/gnokii.h")
    pisitools.insinto("/usr/include/gnokii", "include/gnokii/*")

    # move xgnokii.1x to man1 directory and remove man1x
    pisitools.domove("/usr/share/man/man1x/xgnokii.1x", "/usr/share/man/man1", "xgnokii.1")
    pisitools.removeDir("/usr/share/man/man1x")

    # remove unused man directory
    pisitools.removeDir("/usr/man")

    # remove unused docs
    pisitools.removeDir("/usr/share/doc/gnokii/")

    # install docs
    pisitools.doman("Docs/man/*.1*", "Docs/man/*.8")
    pisitools.dodoc("Docs/README*", "Docs/CREDITS", "Docs/FAQ")

    # we will use our own desktop file and icon
    pisitools.remove("/usr/share/applications/xgnokii.desktop")
