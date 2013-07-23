#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def build():
    # if we are making cross-compiling using arm
    host = get.ARCH().startswith("arm") and autotools.environment["host"] or ""

    autotools.make("CROSSCOMPILE=%s-" % host)

def install():
    autotools.rawInstall("FAKEROOT=%s" % get.installDIR())

    pisitools.insinto("/etc/security", "pam_cap/capability.conf")

    # we should not need this static
    pisitools.remove("/lib/libcap.a")
    pisitools.dodoc("CHANGELOG", "README", "doc/capability.notes")
