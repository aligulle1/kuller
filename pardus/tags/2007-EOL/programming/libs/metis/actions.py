#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="metis-4.0"

def build():
    autotools.make("realclean")
    autotools.make()
   
def install():
    pisitools.dodir("/usr/include/metis")

    pisitools.dodoc("Doc/manual.ps","CHANGES","FILES","VERSION")
    pisitools.dolib("libmetis.a")
   
    for header in ["metis.h","defs.h","struct.h","macros.h","rename.h","proto.h"]:
        shelltools.chmod("Lib/%s" % header, 0644)
        shelltools.copy("Lib/%s" % header, "%s/usr/include/metis/%s" % (get.installDIR(),header))
