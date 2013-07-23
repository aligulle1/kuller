#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cache = [ "ac_cv_func_malloc_0_nonnull=yes",
              "ac_cv_func_realloc_0_nonnull=yes"]

    crosstools.configure("--enable-nls", cache=cache)

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/etc/rsyslog.d")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
