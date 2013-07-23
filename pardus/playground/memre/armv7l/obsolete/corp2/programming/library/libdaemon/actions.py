#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cache = [ "ac_cv_func_malloc_0_nonnull=yes",
              "ac_cv_func_calloc_0_nonnull=yes",
              "ac_cv_func_realloc_0_nonnull=yes",
              "ac_cv_func_setpgrp_void=yes" ]

    autotools.configure("--disable-lynx \
                         --disable-static \
                         --cache-file=config.cache", cache=cache)

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README", "LICENSE")
