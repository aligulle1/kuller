#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get 

WorkDir = "KoboDeluxe-0.4pre10"

def setup():
    pisitools.dosed("configure", "\$\(datadir\)/games/kobo-deluxe", "$(datadir)/kobodeluxe")
    pisitools.dosed("configure", "\$\(prefix\)/games/kobo-deluxe/scores", "$(datadir)/kobodeluxe/scores")
    pisitools.dosed("data/Makefile.in", "\$\(datadir\)/games/kobo-deluxe", "$(datadir)/kobodeluxe")

    autotools.configure("--enable-opengl")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.dodoc("ChangeLog", "README*", "TODO")

