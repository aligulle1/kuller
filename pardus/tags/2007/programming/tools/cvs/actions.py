#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf()
    autotools.configure("--with-tmpdir=/tmp")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("BUGS", "ChangeLog*", "DEVEL*", "FAQ", "HACKING", "MINOR*", "NEWS", "PROJECTS", "README*", "TESTS", "TODO")
