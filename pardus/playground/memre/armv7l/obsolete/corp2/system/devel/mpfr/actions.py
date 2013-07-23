#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools

def setup():
    crosstools.configure("--with-libgmp-prefix=%(RootDir)s/usr \
                          --disable-static" % crosstools.environment)

def build():
    crosstools.make()

def install():
    crosstools.install()

    pisitools.dohtml("FAQ.html")
    pisitools.dodoc("NEWS", "README", "TODO")
