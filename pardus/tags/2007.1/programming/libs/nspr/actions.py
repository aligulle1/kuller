#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("../mozilla/nsprpub/configure \
                       --prefix=/usr \
                       --disable-debug \
                       --enable-optimize=\"%s\"" % get.CFLAGS())

def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/include/nspr/obsolete")
    pisitools.dodir("/usr/include/nspr/private")

    shelltools.copy("dist/lib/*.so","%s/usr/lib" % get.installDIR(), sym=False)
    shelltools.copy("dist/include/nspr/*.h", "%s/usr/include/nspr" % get.installDIR(), sym=False)
    shelltools.copy("dist/include/nspr/obsolete/*.h", "%s/usr/include/nspr/obsolete" % get.installDIR(), sym=False)
    shelltools.copy("dist/include/nspr/private/*.h", "%s/usr/include/nspr/private" % get.installDIR(), sym=False)

    shelltools.copy("config/nspr-config", "%s/usr/bin" % get.installDIR(), sym=False)
