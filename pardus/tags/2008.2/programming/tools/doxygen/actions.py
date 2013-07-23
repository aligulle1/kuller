#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("tmake/lib/linux-g++/tmake.conf", "TMAKE_CFLAGS_RELEASE\s*=.*", "TMAKE_CFLAGS_RELEASE = %s" % get.CFLAGS())
    pisitools.dosed("tmake/lib/linux-g++/tmake.conf", "TMAKE_CXXFLAGS_RELEASE\s*=.*", "TMAKE_CXXFLAGS_RELEASE = %s" % get.CXXFLAGS())
    pisitools.dosed("tmake/lib/linux-g++/tmake.conf", "TMAKE_LFLAGS_RELEASE\s*=.*", "TMAKE_LFLAGS_RELEASE = %s" % get.LDFLAGS())

    autotools.rawConfigure("--prefix %s/usr \
                            --with-doxywizard" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("LANGUAGE.HOWTO", "LICENSE", "README", "VERSION")
