#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make('CC="%(CC)s" \
                    CFLAGS="%(CFLAGS)s -fomit-frame-pointer -DLINUX -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" \
                    LDFLAGS="%(LDFLAGS)s"' % autotools.environment)

def install():
    pisitools.dobin("tree")

    pisitools.doman("man/tree.1")
    pisitools.dodoc("CHANGES", "README*")
