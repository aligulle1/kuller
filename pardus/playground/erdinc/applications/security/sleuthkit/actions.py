#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CC", get.CC())
    shelltools.export("OPT", get.CFLAGS())
    shelltools.system("env -u CFLAGS")
    autotools.make()

def install():
    pisitools.dobin("bin/*")
    pisitools.dodoc("docs/*")
    pisitools.doman("man/man1/*")
    pisitools.dodir("/usr/share/sorter")
    pisitools.insinto("/usr/share/sorter", "share/sorter/*")

# Deny file conflicts
    pisitools.remove("/usr/bin/file")
    pisitools.remove("/usr/bin/dstat")
    pisitools.remove("/usr/share/man/man1/dstat.1")
    pisitools.remove("/usr/share/man/man1/file.1")
