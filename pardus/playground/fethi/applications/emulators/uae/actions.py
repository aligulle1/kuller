#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def install():
    autotools.make()
    pisitools.dobin("uae")
    pisitools.dobin("readdisk")
    pisitools.insinto("/usr/share/uae/amiga-tools", "amiga/*hack")
    pisitools.insinto("/usr/share/uae/amiga-tools", "amiga/trans*")
    pisitools.insinto("/usr/share/uae/amiga-tools", "amiga/uae*")
    pisitools.dodoc("docs/unix/README", "docs/*", "COPYING")