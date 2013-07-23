#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-fvi")

    autotools.configure("--disable-introspection \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    # remove unneeded documentation
    pisitools.removeDir("/usr/doc")
