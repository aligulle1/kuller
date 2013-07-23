#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

#WorkDir = ""

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.removeDir("/etc/init.d")
    pisitools.dosym("/usr/bin/certmaster-sync", "/var/lib/certmaster/triggers/sign/post/certmaster-sync")
    pisitools.dosym("/usr/bin/certmaster-sync", "/var/lib/certmaster/triggers/remove/post/certmaster-sync")
