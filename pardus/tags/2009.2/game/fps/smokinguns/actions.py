#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK / UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

arch = "x86_64" if get.ARCH() == "x86_64" else "i386"

buildDir = "build/release-linux-%s" % arch
dataDir = "/usr/share/smokinguns"

def build():
    autotools.make("DEFAULT_BASEDIR=%s copyfiles" % dataDir)

def install():
    pisitools.insinto("/usr/bin", "%s/smokinguns.%s" % (buildDir, arch), "smokinguns")
    pisitools.insinto("/usr/bin", "%s/smokinguns_dedicated.%s" % (buildDir, arch), "smokinguns-server")

    pisitools.dodoc("BUGS", "ChangeLog", "TODO", "README", "*.txt")
