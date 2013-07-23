#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lbreakout2-2.6beta-7"

def setup():
    autotools.configure('--enable-sdl-net \
                         --localstatedir=/usr/share/lbreakout2 \
                         --with-docdir="/%s/%s"' % (get.docDIR(), get.srcTAG()))
def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")

    pisitools.insinto("/usr/share/pixmaps", "client/gfx/win_icon.png", "lbreakout2.png")
    pisitools.domove("/%s/%s/lbreakout2/" % (get.docDIR(), get.srcTAG()), "/%s/%s/html" % (get.docDIR(), get.srcTAG()))

    pisitools.domo("po/tr.po", "tr", "lbreakout2.mo")

