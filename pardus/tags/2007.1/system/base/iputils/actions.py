#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("Makefile", "(?m)^(CCOPT=.*)-O2", r"\1" + get.CFLAGS())
    pisitools.dosed("Makefile", "(?m)^(CC=.*)gcc", r"\1" + get.CC())
    pisitools.dosed("Makefile", "/usr/src/linux/include", "/usr/include")
    pisitools.dosed("libipsec/Makefile", "/usr/src/linux/include", "/usr/include")
    pisitools.dosed("setkey/Makefile", "/usr/src/linux/include", "/usr/include")

    pisitools.dosed("setkey/Makefile","-ll" ,"-lfl ${LDFLAGS}")
    pisitools.dosed("libipsec/Makefile", "yacc", "bison -y")
    
    autotools.configure()

def build():
    autotools.make()
 
def install():
    autotools.install()

    shelltools.chmod(get.installDIR() + "/bin/ping", 04711)
    shelltools.chmod(get.installDIR() + "/bin/ping6", 04711)

    pisitools.dodoc("INSTALL", "RELNOTES")
    
    pisitools.doman("doc/*.8")
