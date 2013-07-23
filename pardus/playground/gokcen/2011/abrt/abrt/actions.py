# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "abrt"

def setup():
    # We must call this if we're using git tarball
    shelltools.system("bash gen-version")

    autotools.autoreconf("-fi")
    shelltools.system("intltoolize -c -f --automake")

    autotools.configure("--with-pisi")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/var/crash")
    pisitools.dodir("/var/spool/abrt")

    pisitools.dodoc("COPYING", "README", "ChangeLog")
