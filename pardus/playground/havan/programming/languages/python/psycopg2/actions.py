#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/lib/%s/site-packages/" % get.curPYTHON(), "ZPsycopgDA/")
    pisitools.insinto("/usr/lib/%s/site-packages/" % get.curPYTHON(), "psycopg2da/")
    pisitools.insinto("/usr/lib/%s/site-packages/zope" % get.curPYTHON(), "psycopg2da/psycopg2da-configure.zcml")

    pisitools.insinto("/usr/share/doc/psycopg2da-2.0.6-1", "psycopg2da/README.txt")
    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE", "README", "doc/*")
