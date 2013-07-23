#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-%s-src" % (get.srcNAME(), get.srcVERSION())

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    shelltools.export("HOME", get.curDIR())
    autotools.rawInstall("INSTALL_ROOT=%s/usr" % get.installDIR())

