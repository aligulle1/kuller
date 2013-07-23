#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
Skip = ("patches", "pisiBuildState", ".")

def setup():
    for package in shelltools.ls("."):
        if package.startswith(Skip):
            continue

        shelltools.cd(package)
        if package.startswith("xorg-cf-files"):
            pisitools.dosed("host.def", "_PARDUS_CC_",  "%(CC)s" % autotools.environment)
            pisitools.dosed("host.def", "_PARDUS_CXX_", "%(CXX)s" % autotools.environment)
            pisitools.dosed("host.def", "_PARDUS_AS_",  "%(AS)s" % autotools.environment)
            pisitools.dosed("host.def", "_PARDUS_LD_",  "%(LD)s" % autotools.environment)
            pisitools.dosed("host.def", "_PARDUS_CFLAGS_",  "%(CFLAGS)s" % autotools.environment)
            pisitools.dosed("host.def", "_PARDUS_LDFLAGS_", "%(LDFLAGS)s" % autotools.environment)

        autotools.configure("--with-config-dir=/usr/share/X11/config")
        shelltools.cd("../")

def build():
    for package in shelltools.ls("."):
        if package.startswith(Skip):
            continue

        shelltools.cd(package)
        autotools.make()
        shelltools.cd("../")

def install():
    for package in shelltools.ls("."):
        if package.startswith(Skip):
            continue

        shelltools.cd(package)
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")
