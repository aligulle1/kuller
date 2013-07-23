# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#This package using ltdl. .la files should be deleted only for plugins
KeepSpecial = ["libtool"]

def setup():
    arch = get.ARCH()
    extra = ""
    if not arch.startswith("arm"):
        cpu = "x86-64" if arch == "x86_64" else "sse"
        extra = "--with-cpu=%s" % cpu

    pisitools.dosed("configure", "-faltivec")
    autotools.configure('--with-audio="alsa oss" \
                         --with-optimization=2 \
                         --enable-network=yes \
                         --disable-ltdl-install \
                         --with-gnu-ld \
                         %s' % extra)

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README", "AUTHORS")

    pisitools.remove("/usr/lib/libmpg123.la")
