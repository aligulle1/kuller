#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="gmic-%s" % get.srcVERSION()

def setup():
    CFLAGS = "%s -Dcimg_use_lapack" % get.CFLAGS()
    LDFLAGS = "%s -llapack" % get.LDFLAGS()
    # Unused direct dependencies var ama var ama
    autotools.configure()

def build():
    shelltools.cd("src")

    autotools.make("gimp")

def install():
    pisitools.insinto("/usr/lib/gimp/2.0/plug-ins", "./src/gmic_gimp")

    pisitools.dodoc("AUTHORS", "COPYING", "README")
