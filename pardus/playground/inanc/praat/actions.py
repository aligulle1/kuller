#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "sources_5120"

def setup():
    shelltools.copy("%s/sources_5120/makefiles/makefile.defs.linux.dynamic" % get.workDIR(), "%s/sources_5120/makefile.defs" % get.workDIR())
    pisitools.dosed("makefile.defs", "-O", get.CFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/share/praat/test")

    pisitools.dobin("praat")

    pisitools.insinto("/usr/share/praat/test", "test/*")
