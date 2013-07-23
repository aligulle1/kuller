#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "mp4v2-%s" % get.srcVERSION()

# autoreconf breaks sandbox with subversion
shelltools.export("HOME", get.workDIR())

def setup():
    cache = [ "ac_cv_prog_FOUND_HELP2MAN=no", ]

    autotools.autoreconf("-vfi")
    autotools.environment["CXXFLAGS"] = "%(CXXFLAGS)s -lstdc++" % autotools.environment
    autotools.configure("--disable-dependency-tracking \
                         --disable-static \
                         --enable-util \
                         --disable-gch", cache=cache)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "doc/*.txt")

