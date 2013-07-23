#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def build():
    autotools.make("CC=%s \
                    INSTALLROOT=/usr \
                    INCLUDEDIR=/usr/include/gkrellm2 \
                    LOCALEDIR=/usr/share/locale \
                    enable_nls=1 \
                    without-libsensors=yes" % get.CC())

def install():
    autotools.rawInstall("DESTDIR=%s \
                          PREFIX=/usr" % get.installDIR())

    pisitools.insinto("/etc", "server/gkrellmd.conf")

    pisitools.doman("gkrellm.1")
    pisitools.doman("gkrellmd.1")

    pisitools.dodoc("CREDITS", "README", "Changelog", "COPYRIGHT")
    pisitools.dohtml("*")


