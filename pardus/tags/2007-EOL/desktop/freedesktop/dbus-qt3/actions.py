#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    shelltools.system("/usr/lib/python2.4/site-packages/unsermake/unsermake all")

def install():
    shelltools.system("/usr/lib/python2.4/site-packages/unsermake/unsermake DESTDIR=%s install" % get.installDIR())
