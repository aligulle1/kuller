#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "foomatic-filters-3.0-%s" % get.srcVERSION().split("_", 1)[1]

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/bin/foomatic-gswrapper", "/usr/lib/cups/filter/foomatic-gswrapper")
    pisitools.dosym("/usr/bin/foomatic-rip", "/usr/lib/cups/filter/cupsomatic")
    pisitools.dosym("/usr/bin/foomatic-rip", "/usr/bin/lpdomatic")
