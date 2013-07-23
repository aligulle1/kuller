#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="."

def install():
    pisitools.dobin("usr/bin/*")
    pisitools.dolib_so("usr/lib/*")

    pisitools.insinto("/usr/include","usr/include/*")
    pisitools.insinto("/usr/include/Cg","usr/local/Cg/include/*")

    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(),"usr/local/Cg/examples")

    pisitools.doman("usr/share/man/man3/*")
    pisitools.dohtml("usr/local/Cg/docs/html/*")
    pisitools.dodoc("usr/local/Cg/docs/*.pdf", "usr/local/Cg/README", "usr/local/Cg/docs/*.txt")
