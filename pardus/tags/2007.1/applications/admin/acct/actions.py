#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "acct-6.3.5-ts02-12"

def setup():
    autotools.configure("--enable-linux-multiformat")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/account")
    pisitools.remove("/usr/bin/last")
    pisitools.remove("/usr/share/man/man1/last.1")
    
