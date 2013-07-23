#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-database=db \
                         --disable-transactions")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/%s/contrib" % get.srcTAG())
    pisitools.insinto("/usr/share/%s/contrib" % get.srcTAG(), "contrib/*")

    pisitools.dodoc("AUTHORS", "CHANGES*", "COPYING", "INSTALL", "NEWS", "README", \
                    "RELEASE.NOTES*", "TODO", "doc/integrating-with-*")
