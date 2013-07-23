#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "JSBSim"

def setup():
    shelltools.system("./autogen.sh --no-configure")
    autotools.configure()

def build():
    shelltools.system("./autogen.sh --enable-libraries --enable-static --enable-shared")
    autotools.make()

def install():
    autotools.install()

    pisitools.dobin("src/.libs/JSBSim")

    pisitools.insinto("/usr/share/JSBSim/scripts", "scripts/*.xml")

    for root, dirs, files in os.walk("aircraft"):
        for filename in files:
            if filename.endswith(".xml"):
                pisitools.insinto("/usr/share/JSBSim/%s" % root, os.path.join(root, filename))
