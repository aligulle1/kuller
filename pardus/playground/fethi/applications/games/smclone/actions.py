#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "/usr"

def setup():
    pisitools.dosed("bin/smc", "/usr/share/games/smc-0.96", "/usr/share/smclone")

def build():
    pass

def install():
    pisitools.dobin("bin/smc")
    pisitools.insinto("/usr/share/smclone/", "share/games/smc-0.96/*")
    shelltools.system("chmod 755 -R %s/usr/share/smclone" % get.installDIR())
