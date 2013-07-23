#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def build():
    autotools.make("-j1")

def install():
    pisitools.insinto("/usr/share/asleap-%s" % get.srcVERSION(), "scripts")
    pisitools.insinto("/usr/share/asleap-%s" % get.srcVERSION(), "data")

    pisitools.dobin("asleap")
    pisitools.insinto("/usr/bin", "genkeys", "asleap_genkeys")

    pisitools.dodoc("COPYING", "README", "THANKS")
