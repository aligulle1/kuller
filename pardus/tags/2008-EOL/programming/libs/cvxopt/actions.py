#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    shelltools.cd("src")
    pythonmodules.install()

    shelltools.cd("..")
    pisitools.insinto("/usr/share/doc/%s/" % get.srcTAG() , "examples")
    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("doc/*","doc/figures","LICENSE")
