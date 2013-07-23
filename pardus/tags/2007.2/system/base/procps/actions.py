#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "^ALL_CFLAGS += $(call check_gcc,-fweb,)")

def build():
    autotools.make("lib64=/lib CC=%s CPPFLAGS=\"%s\" CFLAGS=\"%s\" LDFLAGS=\"%s\"" % \
                   (get.CC(), get.CXXFLAGS(), get.CFLAGS(), get.LDFLAGS()))

def install():
    autotools.rawInstall("ldconfig=\"true\" DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("sysctl.conf", "BUGS", "NEWS", "TODO", "ps/HACKING")

    pisitools.insinto("/usr/include/proc/", "proc/*.h")

    # conflicts with coreutils
    pisitools.remove("/bin/kill")
    pisitools.remove("/usr/share/man/man1/kill.1")
