#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ladspa_sdk/src"

def setup():
    pisitools.dosed("makefile", "-Wall -Werror -O3", get.CFLAGS())

def build():
    autotools.make('CC="%s" CPP="%s"' % (get.CC(), get.CXX()))

def install():
    autotools.make("INSTALL_PLUGINS_DIR=\"%s/usr/lib/ladspa\" \
                    INSTALL_INCLUDE_DIR=\"%s/usr/include\" \
                    INSTALL_BINARY_DIR=\"%s/usr/bin\" \
                    install" % (get.installDIR(), get.installDIR(), get.installDIR()))

    shelltools.cd("..")
    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("doc/COPYING","doc/ladspa.h.txt")
