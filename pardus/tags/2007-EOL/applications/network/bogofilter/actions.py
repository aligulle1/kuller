#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-database=db \
                         --disable-transactions \
                         --with-included-gsl")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/bogofilter/contrib", "contrib/*")
    pisitools.rename("/etc/bogofilter.cf.example","bogofilter.cf")

    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("AUTHORS", "CHANGES*", "COPYING", "NEWS", "README", "RELEASE.NOTES*", "TODO", "doc/integrating-with-*")
