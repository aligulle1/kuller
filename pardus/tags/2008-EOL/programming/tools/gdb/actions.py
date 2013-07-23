#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-system-readline \
                         --with-separate-debug-dir=/usr/lib/debug \
                         --disable-sim \
                         --disable-rpath \
                         --disable-werror \
                         --with-expat")

def build():
    autotools.make()

def install():
    autotools.install()

    # These come from binutils
    pisitools.removeDir("/usr/lib")
    pisitools.removeDir("/usr/include")

    for info in ["bfd","configure","standards"]:
        pisitools.remove("/usr/share/info/%s.info" % info)

    pisitools.dodoc("CONTRIBUTE", "README", "MAINTAINERS", "NEWS", "ChangeLog*", "TODO")
