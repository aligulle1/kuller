#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

Qt4DIR = get.qtDIR()

def setup():
    shelltools.system("qmake-qt4  PREFIX=%s" % Qt4DIR)

def build():
    autotools.make()
    pisitools.dosed("lib/libqoauth.prl", "^QMAKE_PRL_BUILD_DIR.*", "")

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.dodoc("CHANGELOG", "LICENSE", "README")
