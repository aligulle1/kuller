#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules

WorkDir = "tschellenbach-Django-facebook-ffa8b3e"

def setup():
    pass

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.domove("/usr/README.rest", "/usr/share/doc/Django-facebook/")
    pisitools.domove("/usr/LICENSE.txt", "/usr/share/doc/Django-facebook/")
