#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

def setup():
    # Use our flags
    pisitools.dosed("Makefile", "CFLAGS = -g -O2 -Wall", "CFLAGS = %s" % get.CFLAGS())

def build():
    autotools.make("DESTDIR=%s prefix=/usr" % get.installDIR())

def install():
    autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR())
    autotools.make("DESTDIR=%s prefix=/usr install-doc" % get.installDIR())

    pisitools.dodoc("README", "COPYING", "Documentation/SubmittingPatches")

    perlmodules.fixLocalPod()
