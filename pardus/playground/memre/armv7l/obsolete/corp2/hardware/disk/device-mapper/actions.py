#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "device-mapper.%s" % get.srcVERSION()

def setup():
    cache = [ "ac_cv_func_malloc_0_nonnull=yes",
              "ac_cv_func_calloc_0_nonnull=yes",
              "ac_cv_func_realloc_0_nonnull=yes" ]

    crosstools.configure("--sbindir=/sbin", cache=cache)

def build():
    crosstools.make()

def install():
    crosstools.install('DESTDIR=%(D)s \
                        libdir=%(D)s/lib \
                        includedir=%(D)s/usr/include' % {"D": get.installDIR()})

    libtools.gen_usr_ldscript("libdevmapper.so")
    libtools.gen_usr_ldscript("libdevmapper-event.so")

    pisitools.dodoc("COPYING*", "INTRO", "README", "VERSION", "WHATS_NEW")
