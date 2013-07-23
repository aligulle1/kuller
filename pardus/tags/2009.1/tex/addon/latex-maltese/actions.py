#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir= "maltese"

def build():
    shelltools.system("texi2dvi -q -c --language=latex ./maltese.dtx")

def install():
    for dvidoc in ["maltese.pdf", "maltese.dvi"]:
        print dvidoc
        pisitools.dodoc(dvidoc)
        pisitools.dosym("/usr/share/doc/%s/%s" % (get.srcTAG(), dvidoc), "/usr/share/texmf/doc/latex/%s/%s" % (WorkDir, dvidoc))

    pisitools.insinto("/usr/share/texmf/tex/latex/%s/" % WorkDir, "maltese.sty")

    pisitools.dodoc("README.txt")
