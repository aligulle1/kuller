#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "dvdbackup"

def build():
    autotools.compile("-I/usr/include/dvdread -o dvdbackup src/dvdbackup.c -ldvdread")

def install():
    pisitools.dobin("dvdbackup")
