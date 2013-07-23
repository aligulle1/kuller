#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "apr-util-1.2.7"

def setup():
    autotools.configure("--with-dbm=db42 \
                         --with-berkeley-db=/usr/include/db4.2:/usr/lib \
                         --prefix=/usr \
                         --host=%s \
                         --mandir=/usr/share/man \
                         --infodir=/usr/share/info \
                         --datadir=/usr/share/apr-util-1 \
                         --sysconfdir=/etc \
                         --localstatedir=/var/lib \
                         --with-apr=/usr" % get.CHOST())
def build():
    autotools.make()

def install():
    autotools.install("installbuilddir=%s/usr/share/apr-util-1/build" % get.installDIR())

    # bogus values pointing at /var/tmp/pisi/...
    pisitools.dosed("%s/usr/bin/apu-1-config" % get.installDIR(), \
                    "APU_SOURCE_DIR=.*", \
                    "APU_SOURCE_DIR=/usr/share/apr-util-1")
    pisitools.dosed("%s/usr/bin/apu-1-config" % get.installDIR(), \
                    "APU_BUILD_DIR=.*", \
                    "APU_BUILD_DIR=/usr/share/apr-util-1/build")

    pisitools.domove("/usr/lib/aprutil.exp", "/usr/lib/aprutil1.exp")

    pisitools.dodoc("CHANGES", "LICENSE", "NOTICE")
