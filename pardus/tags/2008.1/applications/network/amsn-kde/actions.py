#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="desktop_integration"
datadir = "/usr/share/amsn/plugins/amsn-kde"
files = ["plugininfo.xml", "desktop_integration.tcl"]

def install():
    for f in files:
        pisitools.insinto(datadir, f)
