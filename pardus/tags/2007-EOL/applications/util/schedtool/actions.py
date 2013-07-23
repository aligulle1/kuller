#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pisitools.dosed("Makefile", "/man/", "/share/man/")
    pisitools.dosed("Makefile", "CFLAGS=-Os -fomit-frame-pointer -s -pipe")

    autotools.make()

def install():
    autotools.rawInstall("DESTPREFIX=%s/usr" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/schedtool/")
    pisitools.dodoc("SCHED_DESIGN", "CHANGES", "INSTALL", "LICENSE", "README", "TUNING")
