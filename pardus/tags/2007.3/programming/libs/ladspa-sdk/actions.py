#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "ladspa_sdk"

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    pisitools.insinto("/usr/bin", "bin/*")
    pisitools.dodir("/usr/include/ladspa")
    pisitools.insinto("/usr/include/ladspa", "src/ladspa.h")
    pisitools.dodir("/usr/lib/ladspa")
    pisitools.insinto("/usr/lib/ladspa", "plugins/*.so")
    pisitools.dosym("/usr/include/ladspa/ladspa.h", "/usr/include/ladspa.h")
