#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

#WorkDir = "puppet-%s" % get.srcVERSION()
shelltools.export("HOME", get.workDIR())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install("--skip-build --root %s" % get.installDIR())

    #files = ["ChangeLog-0.7.10", "ChangeLog-0.7.11","README.w32"]
    #for file in files:
    #    pisitools.remove("/usr/share/doc/buildbot/%s" % file)

    #pisitools.dodoc("ChangeLog-0.7.12", "COPYING", "CREDITS", "NEWS", "README")
