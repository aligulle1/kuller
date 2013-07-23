#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="tls1.5"

def setup():
    autotools.configure("--with-ssl-dir=/usr")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dosed("%s/usr/lib/tls1.50/pkgIndex.tcl" % get.installDIR(), "ifneeded tls 1.5","ifneeded tls 1.50")
