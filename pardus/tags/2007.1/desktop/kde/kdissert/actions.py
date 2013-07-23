#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./waf configure --prefix=%s" % get.kdeDIR())

def build():
    shelltools.system("./waf")

def install():
    shelltools.system("./waf install --destdir=%s" % get.installDIR())
    pisitools.removeDir("%s/share/applnk" % get.kdeDIR())
