#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools

def setup():
    # For world domination and the rest...
    shelltools.export("DO_NOT_COMPILE", "kpovmodeler kmrml kview kuickshow ksvg")

    kde.configure("--with-poppler \
                   --with-kamera")

def build():
    kde.make()

def install():
    kde.install()
