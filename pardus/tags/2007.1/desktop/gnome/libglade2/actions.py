#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "libglade-2.5.1"

def setup():
    shelltools.export("GST_REGISTRY", "%s/registry.xml" % get.curDIR())

    autotools.configure()

    shelltools.export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "")

def build():
    autotools.make()

def install():
    pisitools.dodir("/var/lib/scrollkeeper")

    shelltools.export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "1")

    autotools.install("scrollkeeper_localstate_dir=%s/var/lib/scrollkeeper" % get.installDIR())

    shelltools.export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "")

    pisitools.removeDir("/var/lib/scrollkeeper")
    pisitools.remove("/usr/share/applications/mimeinfo.cache")
