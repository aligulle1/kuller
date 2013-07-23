#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="system-config-printer"

def install():
    pisitools.insinto("/usr/share/system-config-printer", "cupshelpers.py")
    pisitools.insinto("/usr/share/system-config-printer", "debug.py")
    pisitools.insinto("/usr/share/system-config-printer", "ppds.py")

    pisitools.insinto("/etc/dbus-1/system.d", "newprinternotification.conf")

    pisitools.dodoc("README", "AUTHORS", "NEWS", "TODO", "COPYING", "ChangeLog")
