#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    shelltools.system("gcc -o nipper nipper.c")

def install():
    pisitools.dobin("nipper")

    pisitools.insinto("/etc/", "nipper.conf")

    pisitools.doman("man/nipper1", "man/nipper.conf.5")
    pisitools.dodoc("Changelog", "LICENSE", "Readme")
