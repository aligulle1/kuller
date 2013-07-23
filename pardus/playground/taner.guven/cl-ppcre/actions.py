# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    pass

def build():
    pass

def install():
    pisitools.dolib("*.lisp", "usr/share/common-lisp/source/cl-ppcre")
    pisitools.dolib("*.asd", "usr/share/common-lisp/source/cl-ppcre")


    pisitools.dosym("../source/cl-ppcre/cl-ppcre.asd", "usr/share/common-lisp/systems/cl-ppcre.asd")
    pisitools.dosym("../source/cl-ppcre/cl-ppcre-unicode.asd", "usr/share/common-lisp/systems/cl-ppcre-unicode.asd")


