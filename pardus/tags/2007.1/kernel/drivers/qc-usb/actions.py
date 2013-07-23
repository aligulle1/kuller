#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("all PREFIX=%s/usr" % get.installDIR())

def install():
    autotools.rawInstall("all PREFIX=%s/usr MODULE_DIR=%s/lib/modules/%s/extra" % (get.installDIR(),get.installDIR(),get.curKERNEL()))
