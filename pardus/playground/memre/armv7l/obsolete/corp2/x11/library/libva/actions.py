# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #shelltools.export("PKG_CONFIG_SYSROOT_DIR", "%(RootDir)s" % autotools.environment)
    # pkg-config problem
    autotools.environment["CFLAGS"] = "%(CFLAGS)s -I%(RootDir)s/usr/include/libdrm" % autotools.environment
    autotools.autoreconf("-vif")
    autotools.configure("--enable-dummy-driver")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING")
