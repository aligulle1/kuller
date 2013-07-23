#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import get

def setup():
    cache = [ "ac_cv_func_malloc_0_nonnull=yes",
              "ac_cv_func_calloc_0_nonnull=yes",
              "ac_cv_func_realloc_0_nonnull=yes" ]

    autotools.configure("--enable-malloc0returnsnull \
                         --disable-static", cache=cache)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
