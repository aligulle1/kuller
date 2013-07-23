#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get 


def setup():
    pisitools.dosed("Documentation/*.*", "/var/local/iptraf", "/var/lib/iptraf")
    pisitools.dosed("Documentation/*.*", "Documentation", "/usr/share/doc/%s" % get.srcTAG())

def build():
    # To allow ordinary users use iptraf, uncomment the following, but it is a security hole
    # pisitools.chmod("/usr/sbin/iptraf", 4755)
    # shelltools.export("CFLAGS", "%s -DALLOWUSERS" % get.CFLAGS())

    autotools.make('CFLAGS="%s" -C src' % get.CFLAGS())

def install():
    for f in ["src/iptraf", "src/rawtime", "src/rvnamed"]:
        pisitools.dosbin(f)

    pisitools.dodoc("TODO", "README*", "FAQ", "CHANGES", "RELEASE-NOTES")
    pisitools.doman("Documentation/*.8")
    pisitools.dohtml("Documentation/*")

    for d in ["lib", "log", "run"]:
        pisitools.dodir("/var/%s/iptraf" % d)

