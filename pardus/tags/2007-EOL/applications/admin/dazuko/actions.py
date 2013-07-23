#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--without-dep \
                            --disable-local-dpath \
                            --disable-chroot-support \
                            --kernelsrcdir=/lib/modules/%s/source" % get.curKERNEL())

def build():
    autotools.make()

    shelltools.cd("library")
    autotools.make("CC=%s" % get.CC())

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")

    pisitools.dolib("library/libdazuko.a")
    pisitools.insinto("/usr/include", "dazukoio.h")
    pisitools.insinto("/usr/include", "dazuko_events.h")

    pisitools.dodoc("README*", "CHANGELOG")
