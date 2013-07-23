#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-gtk")

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.insinto("/usr/share/pixmaps", "src/xpm/OpenVAS-logo.xpm", "openvas-client.xpm")

    pisitools.dodoc("AUTHORS", "CHANGES", "COPYING", "COPYING.OpenSSL", "COPYING.README", "ChangeLog", "README", "TODO", "VERSION")

    pisitools.dodoc("doc/*.txt")

