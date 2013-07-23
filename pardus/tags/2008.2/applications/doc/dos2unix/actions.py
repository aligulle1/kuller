#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make("clean")
    autotools.make()

def install():
    pisitools.dobin("dos2unix")
    pisitools.dosym("/usr/bin/dos2unix","/usr/bin/mac2unix")

    pisitools.doman("dos2unix.1")
    pisitools.dosym("/usr/share/man/man1/dos2unix.1","/usr/share/man/man1/mac2unix.1")

