#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Fahri Tuğrul Gürkaynak <ftugrul@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="moto4lin"

def setup():
    pisitools.dosed("moto_ui/moto_ui.pro", "/usr/bin", "%s/usr/bin" % get.installDIR())
    shelltools.system("qmake")

def build():
    autotools.make()

def install():
    autotools.install()
    shelltools.chmod("%s/usr/bin/moto4lin" % get.installDIR(), 0755)
    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL*", "NEWS", "README*")

