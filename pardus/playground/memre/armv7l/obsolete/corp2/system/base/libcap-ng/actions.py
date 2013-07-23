#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.unlink("py-compile")
    shelltools.sym("/bin/true", "%s/py-compile" % get.curDIR())

    crosstools.configure("--disable-static")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("program_transform_name= DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING*", "README", "NEWS")
