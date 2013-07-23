#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("dist/Makefile.in", "--optimize 2", "--no-compile")
    pisitools.dosed("src/requestobject.c", "LONG_LONG", "PY_LONG_LONG")

    autotools.autoconf()
    autotools.configure("--with-apxs=/usr/sbin/apxs2")

def build():
    autotools.make("OPT=\"`apxs2 -q CFLAGS` -fPIC\"")

def install():
    autotools.install("DESTDIR=\"%s\"" % get.installDIR())
