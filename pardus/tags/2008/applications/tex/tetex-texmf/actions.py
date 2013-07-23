# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="."
NoStrip="/"

def install():
    pisitools.dodir("/usr/share/texmf")
    pisitools.dodir("/usr/share/texmf-dist")

    files = shelltools.ls("*")
    # since workdir is ".", we have to be careful about pisiBuildState
    files.remove("pisiBuildState")
    for x in files:
         shelltools.copy(x, "%s/usr/share/texmf-dist/%s" % (get.installDIR(), x))

    pisitools.remove("/usr/share/texmf-dist/ls-R")
