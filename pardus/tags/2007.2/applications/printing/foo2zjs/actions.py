#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "foo2zjs"

def setup():
    autotools.make("getweb")
    shelltools.system("./getweb all")

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/share/foomatic/db/source")
    pisitools.dodir("/usr/share/cups/model/foo2zjs")
    autotools.install("DESTDIR=%s" % get.installDIR())
    autotools.install("DESTDIR=%s install-udev" % get.installDIR())

    shelltools.move("%s/usr/share/cups/model/*.ppd.gz" % get.installDIR(), "%s/usr/share/cups/model/foo2zjs/" % get.installDIR())

