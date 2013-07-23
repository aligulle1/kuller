#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("DO_NOT_COMPILE", "kpovmodeler kmrml kview kuickshow ksvg")
    kde.configure("--with-poppler \
                   --with-kamera")

def build():
    kde.make()

def install():
    kde.install()
