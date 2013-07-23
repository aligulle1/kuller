#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    pisitools.doman("vdr.1", "vdr.5")
    pisitools.dobin("vdr")
    pisitools.dobin("svdrpsend.pl")
    pisitools.dodoc("HISTORY", "COPYING", "CONTRIBUTORS")
    pisitools.insinto("/video","*.conf")
