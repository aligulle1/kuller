#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "eciadsl-usermode-0.12"

def setup():
    pisitools.dosed("eciadsl-config.tk", "set BIN_DIR \"/usr/local/bin\"", "set BIN_DIR \"/usr/bin\"")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README", "BUGS", "TODO", "TROUBLESHOOTING")
