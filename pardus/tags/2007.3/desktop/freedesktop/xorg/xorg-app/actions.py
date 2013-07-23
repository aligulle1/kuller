#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # disable -Bdirect
    shelltools.export("LDFLAGS", "")

    # Speed up xkbcomp
    shelltools.export("CFLAGS","%s -DHAVE_STRCASECMP" % get.CFLAGS())

    for package in shelltools.ls("."):
        shelltools.cd(package)
        # Temporary workaround for autohell crap
        # Some packages needs automake-1.10 and 2007 not provides
        # so call autoconf only packages with patches
        if package in ["xsm-1.0.1", "xauth-1.0.2"]:
            autotools.autoconf()
        autotools.configure("--disable-static")
        shelltools.cd("../")

def build():
    for package in shelltools.ls("."):
        shelltools.cd(package)
        autotools.make()
        shelltools.cd("../")

def install():
    for package in shelltools.ls("."):
        shelltools.cd(package)
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")
