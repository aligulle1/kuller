#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir="Imaging-1.1.5"

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/include/%s" % get.curPYTHON(), "libImaging/*.h")
