#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-dynamic")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dohtml("README.html")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "NEWS")

    pisitools.remove("/usr/lib/libadns.a")
