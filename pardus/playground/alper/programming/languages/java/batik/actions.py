#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="batik-%s" % get.srcVERSION()

def setup():
    shelltools.unlinkDir("lib")

def build():
    shelltools.system("sh build.sh all-jar")

def install():
    pisitools.insinto("/usr/share/java", "lib/*.jar")
    pisitools.insinto("/usr/share/java/", "documentation-sources/content/demo/*.jar")

    pisitools.dodoc("LICENSE", "README", "NOTICE", "xdocs/*")
