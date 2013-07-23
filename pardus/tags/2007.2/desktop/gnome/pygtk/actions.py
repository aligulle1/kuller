#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.unlink("py-compile" )
    shelltools.sym("/bin/true", "%s/py-compile" % get.curDIR())

    autotools.configure("--enable-thread \
                         --disable-docs")

    shelltools.touch("%s/style.css" % get.curDIR())
    pisitools.dosed("docs/Makefile", "CSS_FILES = .*", "CSS_FILES = %s/style.css" % get.curDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "MAPPING", "NEWS", "README", "THREADS", "TODO")
