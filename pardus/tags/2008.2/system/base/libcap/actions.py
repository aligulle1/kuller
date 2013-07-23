#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pisitools.dosed("libcap/Makefile", "gperf", "false")

    autotools.make('COPTFLAG="%s" \
                    LDFLAGS="%s" \
                    DEBUG=""' % (get.CFLAGS(), get.LDFLAGS()))

def install():
    autotools.rawInstall("FAKEROOT=%s" % get.installDIR())

    pisitools.dodoc("CHANGELOG", "README", "doc/capability.notes")
