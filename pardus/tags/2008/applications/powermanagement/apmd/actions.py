#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "apmd-3.2.2.orig"

def build():
    pisitools.dosed('Makefile','-I/usr/src/linux/include')
    autotools.make("CC=%s" % get.CC())

def install():
    autotools.rawInstall("DESTDIR=\"%s\" PREFIX=/usr LIBDIR=/usr/lib" % get.installDIR())

    pisitools.doexe("debian/apmd_proxy", "/etc/apm")
    pisitools.dodoc("AUTHORS", "apmsleep.README", "README", "debian/README.Debian", "debian/changelog*", "debian/copyright*")

    pisitools.dodir("/etc/apm/event.d")
    pisitools.dodir("/etc/apm/suspend.d")
    pisitools.dodir("/etc/apm/resume.d")
    pisitools.dodir("/etc/apm/other.d")
    pisitools.dodir("/etc/apm/scripts.d")

    pisitools.doman("*.1", "*.8")

    # we already have one from pm-utils
    pisitools.remove("/usr/bin/on_ac_power")
    pisitools.remove("/usr/share/man/man1/on_ac_power.1")
