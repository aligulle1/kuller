#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

data = "/usr/share/egoboo"
docs = ["change.log", "Egoboodoc.txt"]


def setup():
    for f in docs:
        pisitools.dosed("game/%s" % f, "\r")

    pisitools.dosed("game/Makefile.unix", "^LDFLAGS :=", "LDFLAGS := %s " % get.LDFLAGS())

def build():
    autotools.make('-C game -f Makefile.unix \
                    OPT="%s" \
                    CC="%s"' % (get.CFLAGS(), get.CC()))

def install():
    shelltools.chmod("game/egoboo", 0755)
    pisitools.insinto(data, "game/egoboo")

    for f in docs:
        pisitools.dodoc("game/%s" % f)

