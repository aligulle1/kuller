#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import kde

def setup():
    autotools.make("-f admin/Makefile.common")
    kde.configure("--with-subversion \
                   --with-berkeley-db \
                   --with-db-name=db-4.2 \
                   --with-db-include-dir=/usr/include/db4.2")

def build():
    kde.make()

def install():
    kde.install()
