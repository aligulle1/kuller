#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-nls \
                        --program-prefix=g")
                        
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("gmake", "/usr/bin/make")
    pisitools.dosym("gmake.1","/usr/share/man/man1/make.1")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*")
