#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "open-iscsi-%s-rc4-bnx2i" % get.srcVERSION().replace("_", "-")

def setup():
    shelltools.cd("utils/open-isns")
    autotools.configure()

def build():
    for d in ("utils/open-isns", "utils/sysdeps", "utils/fwparam_ibft",
              "usr", "utils", "libiscsi"):
        autotools.make("OPTFLAGS='%s' -C %s -j1" % (get.CFLAGS(), d))

    shelltools.cd("libiscsi")
    pythonmodules.compile()

def install():
    # First install the executables
    for b in ("usr/iscsid", "usr/iscsiadm", "utils/iscsi-iname", "usr/iscsistart"):
        pisitools.dosbin(b, "/sbin")

    # Install libraries and headers
    pisitools.dolib_so("libiscsi/libiscsi.so.0")
    pisitools.dosym("libiscsi.so.0", "/usr/lib/libiscsi.so")
    pisitools.insinto("/usr/include", "libiscsi/libiscsi.h")

    # Install conf file for the daemon
    pisitools.insinto("/etc/iscsi", "etc/iscsid.conf")

    # Create localstate directories
    pisitools.dodir("/var/lock/iscsi")
    pisitools.dodir("/var/lib/iscsi")
    for d in ("nodes", "send_targets", "static", "isns", "slp", "ifaces"):
        pisitools.dodir("/var/lib/iscsi/%s" % d)

    # Documentation
    pisitools.doman("doc/*.8")
    pisitools.dodoc("Changelog", "COPYING", "README")

    # Install python module
    shelltools.cd("libiscsi")
    pythonmodules.install()

