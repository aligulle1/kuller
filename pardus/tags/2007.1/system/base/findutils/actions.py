#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Don't build or install locate because it conflicts with slocate,
    # which is a secure version of locate.
    pisitools.dosed("Makefile.in", "SUBDIRS = gnulib lib find xargs locate doc po m4", "SUBDIRS = gnulib lib find xargs doc po m4")

    autotools.configure("--enable-nls")

def build():
    autotools.make("libexecdir=/usr/lib/find")

def install():
    autotools.install("libexecdir=%s/usr/lib/find/" % get.installDIR())

    pisitools.removeDir("/var")
    pisitools.dodoc("ChangeLog", "NEWS", "TODO", "README")
