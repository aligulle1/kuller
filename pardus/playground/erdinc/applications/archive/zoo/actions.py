#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "."

def build():
    autotools.make("linux")

def install():
    pisitools.dobin("zoo")
    pisitools.dobin("fiz")
    pisitools.doman("zoo.1")
    pisitools.doman("fiz.1")
