#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir="qbzr"

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/share/pixmaps", "data/bzr-48.png", "bzr.png")

    pisitools.remove("/usr/lib/%s/site-packages/bzrlib/plugins/qbzr/*.txt" % get.curPYTHON())
    pisitools.dodoc("*.txt")
