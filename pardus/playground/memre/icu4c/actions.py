#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="icu/source"

def setup():
    # autoconf version fix, dirty but works :)
    pisitools.dosed("configure.in", r"(^AC_PREREQ).*", r"\1(2.65)")

    shelltools.export('CFLAGS', '%s -fno-strict-aliasing' % get.CFLAGS())
    shelltools.export('CXXFLAGS', '%s -fno-strict-aliasing' % get.CXXFLAGS())

    autotools.autoconf("-f")
    autotools.configure("--with-data-packaging=library \
                         --disable-samples \
                         --disable-tests")

    pisitools.dosed("config/mh-linux", "-nodefaultlibs -nostdlib")

    pisitools.dosed("i18n/Makefile",     r"(^LIBS\s*=).*", r"\1 -L../lib -licuuc -lpthread -lm")
    pisitools.dosed("io/Makefile",       r"(^LIBS\s*=).*", r"\1 -nostdlib -L../lib -licuuc -licui18n -lc")
    pisitools.dosed("layout/Makefile",   r"(^LIBS\s*=).*", r"\1 -nostdlib -L../lib -licuuc -lc")
    pisitools.dosed("layoutex/Makefile", r"(^LIBS\s*=).*", r"\1 -nostdlib -L../lib -licuuc -licule -lc")
    pisitools.dosed("tools/ctestfw/Makefile",  r"(^LIBS\s*=).*", r"\1 -nostdlib -L../../lib -licutu -licuuc -lc")
    pisitools.dosed("tools/toolutil/Makefile", r"(^LIBS\s*=).*", r"\1 -nostdlib -L../../lib -licui18n -licuuc -lpthread -lc")

    if get.ARCH().startswith('arm'):
        # hacky fix for LD_PRELOAD, no clean solution :)
        pisitools.dosed('icudefs.mk.in', r'(^(PKGDATA_|)INVOKE\s*=).*', r'\1')

def build():
    shelltools.export('TARGET', '')
    autotools.make()

def install():
    shelltools.export('TARGET', '')
    autotools.install()

    pisitools.move("%s/usr/sbin/*" % get.installDIR(),"%s/usr/bin" % get.installDIR())
    pisitools.removeDir("/usr/sbin")
