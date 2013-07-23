#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir='sylpheed-3.0.0beta5'

def setup():
    pisitools.dosed("sylpheed.desktop", "Icon=sylpheed", "Icon=sylpheed-128x128")
    autotools.configure("--enable-ldap \
                         --enable-compface \
                         --disable-updatecheck \
                         --disable-static \
                         --with-manualdir=/%s/manual \
                         --with-faqdir=/%s/faq" % (get.docDIR(), get.docDIR()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/pixmaps")
    pisitools.insinto("/usr/share/pixmaps", "*.png")

    pisitools.insinto("/usr/share/applications", "sylpheed.desktop")
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS*", "README*", "TODO*")

