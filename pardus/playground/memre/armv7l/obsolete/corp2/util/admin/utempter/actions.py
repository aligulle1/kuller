#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("LDFLAGS", "%(LDFLAGS)s -Wl,-z,now" % autotools.environment)

    autotools.make('RPM_OPT_FLAGS="%(CFLAGS)s"' % autotools.environment)

def install():
    autotools.rawInstall('RPM_BUILD_ROOT="%s" LIBDIR=/usr/lib' % get.installDIR())
    pisitools.dobin("utmp")
