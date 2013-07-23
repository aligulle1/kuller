#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cache = [ "ac_cv_func_malloc_0_nonnull=yes",
              "ac_cv_func_calloc_0_nonnull=yes",
              "ac_cv_func_realloc_0_nonnull=yes" ]

    # FIXME: device-mapper is not in system.base discuss it
    crosstools.configure("--disable-device-mapper \
                          --disable-static \
                          --without-readline \
                          --enable-Werror=no", cache=cache)

def build():
    crosstools.make('CC="%(CC)s" \
                     LD="%(LD)s" \
                     CFLAGS="%(CFLAGS)s" \
                     LDFLAGS="%(LDFLAGS)s"' % crosstools.environment)

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
    pisitools.dodoc("doc/API", "doc/USER.jp", "doc/FAT")

    pisitools.remove("/usr/bin/label")
    pisitools.removeDir("/usr/bin")
