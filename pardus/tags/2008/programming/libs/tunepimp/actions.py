#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "libtunepimp-%s" % get.srcVERSION()

def setup():
    # do not try to link against obsolete libtermcap
    pisitools.dosed("configure", "-ltermcap", "-lncurses")

    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("python/")
    pythonmodules.install()
    shelltools.cd("..")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")
