#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def build():
    shelltools.cd("django/")
    shelltools.system("bin/compile-messages.py")
    shelltools.cd("../")

    pythonmodules.compile()

def install():
    pythonmodules.install()
