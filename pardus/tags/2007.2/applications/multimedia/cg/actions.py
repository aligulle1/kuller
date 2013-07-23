#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="."

def install():
    pisitools.dobin("usr/bin/*")
    pisitools.dolib("usr/lib/*")

    pisitools.insinto("/usr/include","usr/include/*")
    pisitools.insinto("/usr/include/Cg","usr/local/Cg/include/*")

    pisitools.doman("usr/share/man/man3/*")

    pisitools.dodoc("usr/local/Cg/docs/*.pdf")
    pisitools.dohtml("usr/local/Cg/docs/html/*")

    pisitools.insinto("/usr/share/doc/Cg-%s-%s" % (get.srcVERSION(),get.srcRELEASE()),"usr/local/Cg/docs/txt/*")
    pisitools.insinto("/usr/share/doc/Cg-%s-%s" % (get.srcVERSION(),get.srcRELEASE()),"usr/local/Cg/examples")
