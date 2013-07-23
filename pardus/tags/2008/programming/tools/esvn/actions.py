#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "esvn"

def setup():
    pisitools.dosed("src/mainwindow.cpp", "/usr/share/doc/esvn/html-docs", "/usr/share/doc/%s/html" % get.srcTAG())

def build():
    autotools.make()

def install():
    autotools.rawInstall("-f esvn.mak INSTALL_ROOT=%s install" % get.installDIR())

    pisitools.dobin("esvn")
    pisitools.dobin("esvn-diff-wrapper")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
    pisitools.dohtml("html-docs/*")
