#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import texlivemodules

from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().split("_")[-1])

def build():
    texlivemodules.compile()

def install():
    texlivemodules.install()

    # Install texmf bin scripts

    bindocs=["thumbpdf/thumbpdf.pl","oberdiek/pdfatfi.pl"]

    pisitools.dosym("/usr/share/texmf-dist/scripts/thumbpdf/thumbpdf.pl", "/usr/bin/thumbpdf" )
    pisitools.dosym("/usr/share/texmf-dist/scripts/oberdiek/pdfatfi.pl", "/usr/bin/pdfatfi" )
