#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
    autotools.make("-j1")
    shelltools.cd("../dbm")
    autotools.make("-j1")
    shelltools.cd("../nss")
    autotools.make("-j1")


def install():
    for binary in ["certutil","modutil","pk12util","signtool","ssltap"]:
        pisitools.insinto("/usr/bin","dist/Linux*/bin/%s" % binary, sym=False)

    # Shared libs
    for library in ["libnss3.so","libnssckbi.so","libsmime3.so","libsoftokn3.so","libsoftokn3.chk","libssl3.so","libfreebl3.so","libfreebl3.chk"]:
        pisitools.insinto("/usr/lib/nss","dist/Linux*/lib/%s" % library, sym=False)

    # Static libs
    for library in ["libcrmf.a","libnssb.a","libnssckfw.a"]:
        pisitools.insinto("/usr/lib/nss","dist/Linux*/lib/%s" % library, sym=False)

    # Headers
    for header in ["dist/private/nss/*.h","dist/public/nss/*.h"]:
        pisitools.insinto("/usr/include/nss", header, sym=False)
