#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    shelltools.export("CC", get.CC())
    autotools.make("-j1")

def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING.LIB", "README*", "TODO")
