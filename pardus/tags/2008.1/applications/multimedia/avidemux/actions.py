#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir = 'avidemux_%s' % get.srcVERSION()

def setup():
    cmaketools.configure()

def build():
    autotools.make("-j1")

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "avidemux_icon.png", "avidemux.png")

    pisitools.dodoc("COPYING", "History", "AUTHORS")
