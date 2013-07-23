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

WorkDir="nss-%s/mozilla" % get.srcVERSION()

def build():
    shelltools.export("BUILD_OPT","1")
    shelltools.export("NSS_ENABLE_ECC","1")
    shelltools.export("CFLAGS","%s -g -fno-strict-aliasing" % get.CFLAGS())

    shelltools.cd("security/coreconf")
    autotools.make()
    shelltools.cd("../dbm")
    autotools.make()
    shelltools.cd("../nss")
    autotools.make()


def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/lib/nss")
    pisitools.dodir("/usr/include/nss")

    for binary in ["certutil","modutil","pk12util","signtool","ssltap"]:
        shelltools.copy("dist/Linux*/bin/%s" % binary, "%s/usr/bin" % get.installDIR(), sym=False)

    # Shared libs
    for library in ["libnss3.so","libnssckbi.so","libsmime3.so","libsoftokn3.so","libsoftokn3.chk","libssl3.so","libfreebl3.so","libfreebl3.chk"]:
        shelltools.copy("dist/Linux*/lib/%s" % library,"%s/usr/lib/nss" % get.installDIR(), sym=False)

    # Static libs
    for library in ["libcrmf.a","libnssb.a","libnssckfw.a"]:
        shelltools.copy("dist/Linux*/lib/%s" % library, "%s/usr/lib/nss" % get.installDIR(), sym=False)

    shelltools.copy("dist/private/nss/*.h", "%s/usr/include/nss" % get.installDIR(), sym=False)
    shelltools.copy("dist/public/nss/*.h", "%s/usr/include/nss" % get.installDIR(), sym=False)
