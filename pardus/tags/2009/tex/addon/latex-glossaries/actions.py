#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir= "glossaries"

def build():
    shelltools.system("latex --interaction=batchmode ./glossaries.ins")
    shelltools.system("texi2dvi -q -c --language=latex ./glossaries.dtx")

def install():
    pisitools.insinto("/usr/share/texmf/tex/latex/%s/" % WorkDir, "*.sty")

    pisitools.dobin("makeglossaries")
    pisitools.insinto("/usr/share/texmf-site/tex/latex/%s/dict/" % WorkDir, "*.dict")

    for dvidoc in shelltools.ls("*.pdf"):
        print dvidoc
        pisitools.dodoc(dvidoc)
        pisitools.dosym("/usr/share/doc/%s/%s" % (get.srcTAG(), dvidoc), "/usr/share/texmf/doc/latex/%s/%s" % (WorkDir, dvidoc))

    pisitools.insinto("/usr/share/doc/%s/examples/" % get.srcTAG(), "*.tex")
    pisitools.dodoc("README", "CHANGES")
