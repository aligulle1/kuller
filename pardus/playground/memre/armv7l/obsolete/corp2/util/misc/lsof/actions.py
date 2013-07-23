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

WorkDir = "lsof_%s_src" % get.srcVERSION()

def setup():
    shelltools.touch(".neverInv")
    shelltools.system("./Configure linux")

    pisitools.dosed("lib/Makefile", r"(^RANLIB\s*=\s*)ranlib(.*)$", "\\1 %(RANLIB)s \\2" % autotools.environment)
    pisitools.dosed("lib/Makefile", r"(^AR\s*=\s*)ar(.*)$", "\\1 %(AR)s \\2" % autotools.environment)

def build():
    autotools.make('CC="%(CC)s" \
                    INCL="%(CFLAGS)s" \
                    DEBUG= all' % autotools.environment)

def install():
    pisitools.dosbin("lsof")

    pisitools.insinto("/usr/share/lsof/scripts", "scripts/*")

    pisitools.doman("lsof.8")
    pisitools.dodoc("00*")
