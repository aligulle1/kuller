# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    for dir in ["base","emulation","extensions","themes"]:
        pisitools.insinto("/usr/share/texmf-dist/latex-beamer",dir)

    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "examples")
    pisitools.dodoc("README","ChangeLog","doc/*.pdf")

