#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
WorkDir = "."

def build():
    shelltools.cd("scintilla/gtk")
    autotools.make()

    shelltools.cd("../../scite/gtk")
    autotools.make()

def install():
    shelltools.cd("scite/gtk")
    autotools.install()

    shelltools.cd("../../")
    pisitools.insinto("/usr/share/doc/scite", "scite/README","scite-README")
    pisitools.insinto("/usr/share/doc/scite", "scintilla/README","scintilla-README")
    pisitools.insinto("/usr/share/doc/scite/scite", "scite/doc/*")
    pisitools.insinto("/usr/share/doc/scite/scintilla", "scintilla/doc/*")

    pisitools.dodoc("scite/License.txt")
    pisitools.doman("scite/doc/scite.1")
    pisitools.dosym("/usr/bin/SciTE","/usr/bin/scite")

