#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cache = [ "ac_cv_func_malloc_0_nonnull=yes",
              "ac_cv_func_realloc_0_nonnull=yes" ]
    crosstools.configure("--bindir=/bin \
                         --enable-nls", cache=cache)

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    for file in shelltools.ls("%s/bin" % get.installDIR()):
        pisitools.dosym("/bin/%s" % file, "/usr/bin/%s" % file)

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
