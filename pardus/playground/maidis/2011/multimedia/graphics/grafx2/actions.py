#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "grafx2"

def build():
    shelltools.cd("src")

    autotools.make()

def install():
    shelltools.cd("src")

    autotools.rawInstall("prefix=\"/usr\" DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("../doc/*")
