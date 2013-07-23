# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "asdf"

def setup():
    pass

def build():
    pass

def install():
    SOURCE_DIR = "/usr/share/common-lisp/source/cl-asdf"

    pisitools.doexe("asdf.lisp", SOURCE_DIR)
    pisitools.dolib("asdf-ecl.lisp", SOURCE_DIR)
    pisitools.dolib("wild-modules.lisp", SOURCE_DIR)
    pisitools.dolib("asdf.asd", SOURCE_DIR)
    pisitools.dolib("build.xcvb", SOURCE_DIR)
