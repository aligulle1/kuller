#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) TUBITAK / UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.system("perl makeunidef.pl --nocomments -t data -d \
                       /usr/lib/perl5/%s/unicore/UnicodeData.txt \
                       config/*.ucf.gz" % get.curPERL())

def install():
    for files in ("config", "contrib", "data", "*.def", "*.sty"):
        pisitools.insinto("/usr/share/texmf-dist/tex/latex/latex-unicode/", files)

    pisitools.dodoc("FAQ", "LICENSE", "README", "VERSION", "*.txt")
