#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('NO_ARLIB=1 \
                    LIBDIR=%(RootDir)s/lib \
                    USRLIBDIR=%(RootDir)s/usr/lib \
                    NO_GLIBC_KEYERR=1 \
                    CFLAGS="%(CFLAGS)s"' % autotools.environment)

def install():
    autotools.install("NO_ARLIB=1 LIBDIR=/lib USRLIBDIR=/usr/lib DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENCE.GPL", "LICENCE.LGPL", "README")
