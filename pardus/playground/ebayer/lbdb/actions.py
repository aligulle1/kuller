#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

#WorkDir = ""

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-evolution-addressbook-export=/usr/libexec/evolution/2.32/evolution-addressbook-export \
                         --sysconfdir=/etc/lbdb \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install("sysconfdir=%s/etc/lbdb" % get.installDIR())
