#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "%s-%s-final" % (get.srcNAME(), get.srcVERSION())

def build():
    shelltools.cd("django/")
    shelltools.system("bin/compile-messages.py")
    shelltools.cd("../")

    pythonmodules.compile()

def install():
    pythonmodules.install()
