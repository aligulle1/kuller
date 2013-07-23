#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def build():
    # Suggested C(XX)FLAGS by the upstream author
    shelltools.export("CFLAGS","%s -O3 -fomit-frame-pointer -funroll-loops" % get.CFLAGS())
    shelltools.export("CXXFLAGS","%s -O3 -fomit-frame-pointer -funroll-loops" % get.CXXFLAGS())

    autotools.make()

def install():
    autotools.install("prefix=%s/usr mandir=%s/usr/share/man docdir=%s/usr/share/doc" %
                   (get.installDIR(), get.installDIR(), get.installDIR()))
