#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "freetds-0.91"

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--with-tdsver=0.8 \
                         --with-unixODBC=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("usr/lib/*.a")

    # Keep doc files under doc dir named as source name, not as WorkDir
    pisitools.domove("/usr/share/doc/%s/*" % WorkDir, "/usr/share/doc/%s" % get.srcNAME())
    pisitools.removeDir("/usr/share/doc/%s" % WorkDir)

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
