# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # Fix python .pc filename
    pisitools.dosed("configure.ac", r"PKG_CHECK_MODULES\(\[PYTHON\], \[python\]", "PKG_CHECK_MODULES([PYTHON], [python-%s]" % get.curPYTHON().replace("python", ""))

    autotools.autoreconf("-fi")
    shelltools.system("intltoolize -c -f --automake")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING")
