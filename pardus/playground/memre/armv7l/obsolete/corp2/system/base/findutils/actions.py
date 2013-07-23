#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools

def setup():
    crosstools.environment["CFLAGS"] = "%s -D_GNU_SOURCE" % crosstools.environment["CFLAGS"]

    cache = [ "gl_cv_func_wcwidth_works=yes",
              "gl_cv_header_working_fcntl_h=yes",
              "ac_cv_func_fnmatch_gnu=yes" ]

    crosstools.configure("--enable-nls \
                          --without-internal-regex \
                          --disable-rpath \
                          --disable-assert \
                          --enable-d_type-optimization", cache=cache)

def build():
    crosstools.make()

def install():
    crosstools.install()

    pisitools.dodoc("ChangeLog", "NEWS", "TODO", "README")
