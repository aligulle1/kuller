#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --with-documentation=%s/usr/share/doc/libupnp-%s-%s" % (get.installDIR(),get.srcVERSION(),get.srcRELEASE()))

def build():
    autotools.make()

def install():
    autotools.install()
