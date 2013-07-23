#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("-f makefile.unx")
    autotools.make("-f makefile.unx xfilerepair")

def install():
    pisitools.dobin("filerepair")
    pisitools.dobin("xfilerepair")
    pisitools.insinto("/usr/share/pixmaps", "filerepair.xpm")
    pisitools.dodoc("CONTENTS", "COPYING", "INSTALL", "README")
    pisitools.dohtml("help/*")

