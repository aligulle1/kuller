#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "apr-1.2.7"

def setup():
    autotools.rawConfigure("--enable-ipv6 \
                            --enable-threads \
                            --enable-nonportable-atomics \
                            --prefix=/usr \
                            --host=%s \
                            --mandir=/usr/share/man \
                            --infodir=/usr/share/info \
                            --datadir=/usr/share/apr-1 \
                            --sysconfdir=/etc \
                            --localstatedir=/var/lib" % get.CHOST())
def build():
    autotools.make()

def install():
    autotools.install("installbuilddir=%s/usr/share/apr-1/build" % get.installDIR())

    # bogus values pointing at /var/tmp/pisi/...
    pisitools.dosed("%s/usr/bin/apr-1-config" % get.installDIR(), \
                    "APR_SOURCE_DIR=.*", \
                    "APR_SOURCE_DIR=/usr/share/apr-1")
    pisitools.dosed("%s/usr/bin/apr-1-config" % get.installDIR(), \
                    "APR_BUILD_DIR=.*", \
                    "APR_BUILD_DIR=/usr/share/apr-1/build")
    pisitools.dosed("%s/usr/bin/apr-1-config" % get.installDIR(), \
                    "installbuilddir=.*", \
                    "installbuilddir=/usr/share/apr-1/build")
    pisitools.dosed("%s/usr/bin/apr-1-config" % get.installDIR(), \
                    "CPPFLAGS=\"\\(.*\\)\"", \
                    "CPPFLAGS=\"\\1 -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE\"")

    pisitools.dosed("%s/usr/share/apr-1/build/apr_rules.mk" % get.installDIR(), \
                    "apr_builddir=.*", \
                    "apr_builddir=/usr/share/apr-1/build")
    pisitools.dosed("%s/usr/share/apr-1/build/apr_rules.mk" % get.installDIR(), \
                    "apr_builders=.*", \
                    "apr_builders=/usr/share/apr-1/build")

    pisitools.domove("/usr/lib/apr.exp", "/usr/lib/apr1.exp")

    pisitools.insinto("/usr/share/apr-1/build", "build/*.awk")
    pisitools.insinto("/usr/share/apr-1/build", "build/*.sh")
    pisitools.insinto("/usr/share/apr-1/build", "build/*.pl")

    pisitools.dodoc("CHANGES", "LICENSE", "NOTICE")
