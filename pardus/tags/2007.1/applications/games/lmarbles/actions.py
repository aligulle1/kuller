#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get 


def setup():
    pisitools.dosed("src/Makefile.in", "/marbles.prfs", "/lmarbles.prfs")
    pisitools.dosed("src/lmarbles.6", "/marbles.prfs", "/lmarbles.prfs")

    autotools.configure("--localstatedir=/usr/share/lmarbles")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")
    pisitools.insinto("/usr/share/pixmaps", "lmarbles48.gif")
