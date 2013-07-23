#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "module-init-tools-3.3-pre11"

def setup():
    autotools.autoreconf("-fi")
    autotools.automake()
    autotools.configure("--enable-zlib")

def build():
    autotools.make()

def install():
    autotools.install("prefix=%s" % get.installDIR())

    # remove useless static linked one, we are using busybox one...
    pisitools.remove("/sbin/insmod.static")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
