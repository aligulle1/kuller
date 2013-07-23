#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("DO_NOT_COMPILE","umbrello")
    
    kde.configure("--with-subversion \
                   --with-berkeley-db \
                   --with-db-name=db-4.2 \
                   --with-db-include-dir=/usr/include/db4.2")

def build():
    kde.make()

def install():
    kde.install()
