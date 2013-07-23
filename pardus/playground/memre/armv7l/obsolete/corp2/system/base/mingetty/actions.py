#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mingetty-1.0.7s"

def build():
    # FIXME: optimization flags
    crosstools.environment["CFLAGS"] = "-O3 -march=armv7-a -mtune=cortex-a8 -mfpu=neon -mfpu=vfp -mfloat-abi=softfp \
                                        -I%(SysRoot)s/usr/include" % crosstools.environment
    crosstools.make('CC="%(CC)s" \
                     RPM_OPT_FLAGS="%(CFLAGS)s" \
                     LD="%(LD)s" \
                     LDFLAGS="%(LDFLAGS)s"' % crosstools.environment)

def install():
    pisitools.dosbin("mingetty", "/sbin")
    pisitools.doman("mingetty.8")
    pisitools.insinto("/usr/share/locale/tr/LC_MESSAGES", "tr.mo", "mingetty.mo")

    pisitools.dodoc("ANNOUNCE", "COPYING", "TODO", "CHANGES")
