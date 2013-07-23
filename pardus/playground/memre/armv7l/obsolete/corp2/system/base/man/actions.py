#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    crosstools.prepare()
    autotools.rawConfigure("-confdir=/etc +fhs +fsstnd +traditional +lang all")

    shelltools.system("%(HOSTCC)s src/makemsg.c -o src/makemsg" % crosstools.environment)

def build():
    crosstools.make("nls=all")

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/man", "/usr/share")

    pisitools.dodoc("README")
