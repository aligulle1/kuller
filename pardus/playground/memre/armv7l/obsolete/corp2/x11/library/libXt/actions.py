#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static")

    # preparing host-side utils
    autotools.make('-C util \
                    CC_FOR_BUILD="%(HOSTCC)s" \
                    CFLAGS="%(HOSTCFLAGS)s"' % autotools.environment)
    shelltools.system("mv util/{,host}makestrs; make -C util clean")

def build():
    autotools.make('CC="%(CC)s" ' % autotools.environment)

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin("util/makestrs", "/usr/bin")
