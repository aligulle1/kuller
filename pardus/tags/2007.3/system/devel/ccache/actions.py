#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dobin("ccache")

    pisitools.doman("ccache.1")
    pisitools.dodoc("README")
    pisitools.dohtml("web/")

    pisitools.dodir("/usr/lib/ccache/bin")
