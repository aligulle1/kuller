#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/share/foomatic/db/source")
    pisitools.dodir("/usr/share/cups/model/foo2zjs")

    autotools.install("DESTDIR=%s install-udev" % get.installDIR())
