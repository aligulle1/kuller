#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir="mongodb-mongo-python-driver-2bb4d67"

def build():
    pythonmodules.compile("doc")

def install():
    pythonmodules.install()

    pisitools.dohtml("doc/_build/1.7/*")