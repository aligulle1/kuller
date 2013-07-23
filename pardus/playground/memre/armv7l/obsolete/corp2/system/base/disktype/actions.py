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

def build():
    shelltools.export("CCACHE_DIR", "%s" % get.workDIR())
    crosstools.make('CC="%(CC)s" \
                     CFLAGS="%(CFLAGS)s -fno-stack-protector -fno-strict-aliasing"' % crosstools.environment)

def install():
    pisitools.dobin("disktype")
    pisitools.doman("disktype.1")
    pisitools.dodoc("README", "HISTORY", "TODO")
