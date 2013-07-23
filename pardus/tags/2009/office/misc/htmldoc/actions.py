#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/share/htmldoc/data")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.removeDir("/usr/share/doc/htmldoc")

    pisitools.dohtml("doc/*.html")
    pisitools.dohtml("doc/*.png")

    pisitools.insinto("/usr/share/applications", "desktop/htmldoc.desktop")
    pisitools.insinto("/usr/share/icons/", "desktop/htmldoc-48.png")
