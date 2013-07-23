#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="kqemu-%s" % get.srcVERSION().replace('_','')

def setup():
    pisitools.dosed("configure", "`uname -r`", get.curKERNEL())
    pisitools.dosed("install.sh", "`uname -r`", get.curKERNEL())
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")

    pisitools.dodoc("README")
    pisitools.dohtml("kqemu-doc.html")

