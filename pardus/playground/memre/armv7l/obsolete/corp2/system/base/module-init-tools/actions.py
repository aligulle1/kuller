#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "module-init-tools-%s" % get.srcVERSION().replace("_", "-")

def setup():
    # Disable man pages
    pisitools.dosed("Makefile.am", r"^dist_man_MANS\s*=\s*.*$", "")

    crosstools.environment["CFLAGS"] = crosstools.environment["CFLAGS"].replace("-O2", "-Os -g -DCONFIG_NO_BACKWARDS_COMPAT=1")
    crosstools.autoreconf("-fi")

    crosstools.configure()
    #crosstools.configure("--enable-zlib-dynamic --disable-static-utils")

def build():
    crosstools.make()

def install():
    crosstools.install("program_transform_name= prefix=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
