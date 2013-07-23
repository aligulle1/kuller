#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "qtreactor"

def install():
    pisitools.insinto("/usr/lib/%s/site-packages/twisted/internet" % get.curPYTHON(), "qt4reactor.py")
    pisitools.insinto("/usr/lib/%s/site-packages/twisted/plugins" % get.curPYTHON(), "twisted/plugins/qt4.py")

    pisitools.dodoc("README")
