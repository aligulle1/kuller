#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

WorkDir = "lila-0.8.5-beta"

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    pisitools.insinto("/etc", "lila.cfg")
    pisitools.dobin("lila")
    pisitools.dodoc("CHANGELOG", "LICENSE", "README")

