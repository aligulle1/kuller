#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("DEFS", "NO_ASM")
    crosstools.configure("--exec-prefix=/")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    # add missing gzcat
    pisitools.dosym("zcat", "/bin/gzcat")

    pisitools.dodoc("ChangeLog", "NEWS", "README", "THANKS", "TODO")
