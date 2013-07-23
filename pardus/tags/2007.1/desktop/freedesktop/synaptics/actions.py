#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "INSTALLED_X = .*", "INSTALLED_X = $(DESTDIR)/usr/")
    pisitools.dosed("Makefile", "BINDIR = .*/usr/local/bin", "BINDIR = %s/usr/bin" % get.installDIR())
    pisitools.dosed("Makefile", "MANDIR = .*", "MANDIR = %s/usr/share/man" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/lib/modules/input/synaptics_drv.o", "/usr/lib/xorg/modules/input/")
    pisitools.domove("/usr/local/bin/synclient","/usr/bin/")
    pisitools.domove("/usr/local/bin/syndaemon","/usr/bin/")
