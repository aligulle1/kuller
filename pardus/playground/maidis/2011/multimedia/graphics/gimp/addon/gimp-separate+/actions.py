#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())

    pisitools.insinto("/usr/share/gimp/2.0/scripts", "sample-scripts/*")
    pisitools.insinto("/usr/share/color/icc", "sRGB/*.icc")

    shelltools.chmod("%s/usr/share/color/icc/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/gimp/2.0/scripts/*" % get.installDIR(), 0644)

    pisitools.dodoc("COPYING", "README*", "readme*", "sRGB/*.txt")
