#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('FLINT_TUNE="%s" \
                    FLINT_GMP_LIB_DIR=/usr/lib \
                    FLINT_LINK_OPTIONS="%s" libflint.so' % (get.CFLAGS(),get.LDFLAGS()))

def install():
    pisitools.dolib("libflint.so")

    for header in ["flint.h","longlong_wrapper.h"]:
        pisitools.insinto("/usr/include/flint", header)

    pisitools.dodoc("doc/*.pdf")
    pisitools.dodoc("CHANGES.txt","gpl-2.0.txt","todo.txt")
