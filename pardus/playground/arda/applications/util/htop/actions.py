#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "htop-0.6.3"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALLROOT=%s" % get.installDIR())
    pisitools.dodoc("README", "CHANGES", )        
