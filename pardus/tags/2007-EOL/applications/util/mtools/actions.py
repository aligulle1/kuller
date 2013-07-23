#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--sysconfdir=/etc/mtools \
                         --with-x \
                         --disable-floppyd")

def build():
    autotools.make()

def install():
    autotools.install("sysconfdir=%s/etc/mtools" % get.installDIR())
    pisitools.insinto("/etc/mtools","mtools.conf")

    pisitools.dodoc("Changelog", "NEWPARAMS", "README*", "Release.notes")
