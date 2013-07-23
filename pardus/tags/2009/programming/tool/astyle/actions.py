#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) TUBITAK / UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "astyle"

def build():
    shelltools.cd("buildgcc")
    autotools.make("release shared")

def install():
    shelltools.cd("buildgcc")
    autotools.install()

    pisitools.dohtml("../doc/*.html")
