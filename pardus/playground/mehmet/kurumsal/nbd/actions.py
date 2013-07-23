#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.configure()

def build():
    autotools.make()
    shelltools.cd("doc")
    shelltools.system("doxygen")

def install():
    autotools.install()
    pisitools.dohtml("doc/doxygen-output/html/*")
    pisitools.dodoc("README")
    pisitools.dobin("gznbd/gznbd")
