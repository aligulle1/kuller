#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def setup():
    pass

def build():
    shelltools.export("LC_ALL", "C")
    ANT_OPTs = ("-Dext.binaries.downloaded=true,\
                -Dcluster.config=basic,\
                -f nbbuild/build.xml build-nozip")
    shelltools.system("ant")

def install():
    pisitools.dobin("nbbuild/netbeans/bin/netbeans")

