#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="ruby-1.8.5-p2"

def setup():
    shelltools.export("CFLAGS", get.CFLAGS().replace("-fomit-frame-pointer", ""))
    shelltools.export("CXXFLAGS", get.CXXFLAGS().replace("-fomit-frame-pointer", ""))

    autotools.configure("--enable-shared \
                         --enable-pthread")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s install-doc" % get.installDIR())

    # No static libs
    pisitools.remove("/usr/lib/libruby-static.a")

    pisitools.dodoc("COPYING*", "ChangeLog", "MANIFEST", "README*", "ToDo")
