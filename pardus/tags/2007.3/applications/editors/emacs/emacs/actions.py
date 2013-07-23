#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-gtk")

def build():
    autotools.make("bootstrap")

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "BUGS", "README")
