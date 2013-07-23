#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="crm114-20070810-BlameTheSegfault.src"

def build():
    shelltools.export("OS_CFLAGS",get.CFLAGS())

    pisitools.dosed('mailfilter.cf','#:mime_decoder: /normalizemime/',':mime_decoder: /normalizemime/')
    autotools.make("-j1")

def install():
    autotools.install()

    for files in ["*.crm","*.cf","*.mfp"]:
        pisitools.insinto("/usr/share/crm114",files)

    pisitools.dodoc("COLOPHON.txt","CRM114_Mailfilter_HOWTO.txt","FAQ.txt","INTRO.txt",
                    "QUICKREF.txt","classify_details.txt","inoc_passwd.txt",
                    "knownbugs.txt","things_to_do.txt","README")
