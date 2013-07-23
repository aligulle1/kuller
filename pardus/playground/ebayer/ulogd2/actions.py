#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

WorkDir = "ulogd-2.0.0beta4"

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.insinto("/etc/", "ulogd.conf")
    pisitools.insinto("/etc/logrotate.d/", "ulogd.logrotate", "ulogd")
    pisitools.dodoc("doc/*", "AUTHORS", "COPYING", "README", "TODO")

