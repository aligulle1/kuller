#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,207 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="kqemu-1.3.0pre11"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")

    pisitools.dodoc("README")
    pisitools.dohtml("kqemu-doc.html")

