#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "gnubg"

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure()


def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "TODO", "NEWS", "COPYING")
