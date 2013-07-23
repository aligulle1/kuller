#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "puppet-%s" % get.srcVERSION()
shelltools.export("HOME", get.workDIR())

print ":::::::::::"
print get.workDIR()

def setup():
    pass

def build():
    pass

def install():
    shelltools.system("ruby install.rb install --destdir=%s" % get.installDIR())
    pass

