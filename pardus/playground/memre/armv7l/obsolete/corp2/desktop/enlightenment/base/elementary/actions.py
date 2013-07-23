#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--with-gnu-ld \
                         --disable-static \
                         --with-edje-cc=/usr/bin/edje_cc \
                         --with-eet-eet=/usr/bin/eet")
    pisitools.dosed("libtool", r"\s+(/usr/lib)", " %(SysRoot)s\\1" % autotools.environment)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "README")
