#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf()
    autotools.configure("--with-tmpdir=/tmp")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("BUGS", "ChangeLog*", "FAQ", "NEWS", "README*")
