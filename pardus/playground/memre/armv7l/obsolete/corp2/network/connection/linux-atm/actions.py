#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "linux-atm-%s" % get.srcVERSION()

def setup():
    crosstools.environment["CXXFLAGS"] = ""
    crosstools.environment["CFLAGS"] = "%s -fno-strict-aliasing" % crosstools.environment["CFLAGS"]

    pisitools.dosed("src/Makefile.in", "br2684", "")
    crosstools.configure()

def build():
    # Host-side preparations
    for q in [ "qgen q.dump", "all" ]:
        crosstools.environment["q"] = q
        crosstools.make('-C src/qgen \
                        AR="%(HOSTAR)s" \
                        CPP="%(HOSTCPP)s" \
                        CC="%(HOSTCC)s" \
                        CXX="%(HOSTCXX)s" \
                        LD="%(HOSTLD)s" \
                        CFLAGS="%(HOSTCFLAGS)s" \
                        CXXFLAGS="%(HOSTCXXFLAGS)s" \
                        DEFS="-Isrc -I. -I../.. -DHAVE_CONFIG_H" \
                        %(q)s' % crosstools.environment)

    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s man_prefix=/usr/share/man \
                           program_transform_name=" % get.installDIR())
    pisitools.insinto("/etc", "src/config/hosts.atm")

    pisitools.dodoc("AUTHORS", "THANKS", "ChangeLog", "BUGS", "NEWS", "README")
