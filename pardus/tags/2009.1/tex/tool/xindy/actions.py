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
import os

#os.environ["HOME"]=get.installDIR()
def setup():
     autotools.configure("--enable-external-clisp\
                          --enable-clisp-dir=/usr/lib/clisp-2.48")

def build():
    shelltools.export("VARTEXFONTS", get.curDIR())
    autotools.make("-j1")

def install():
     autotools.rawInstall("DESTDIR=%s" % get.installDIR())
     pisitools.dodoc("AUTHORS", "ChangeLog.Gour", "NEWS", "README")
     pisitools.domove("/usr/share/doc/%s/*" % get.srcDIR(), "/usr/share/doc/%s/" % get.srcNAME())

