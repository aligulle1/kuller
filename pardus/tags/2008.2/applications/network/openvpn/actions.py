#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-pthread \
                         --enable-ssl \
                         --enable-crypto")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodir("/etc/openvpn")
    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.GPL", "ChangeLog", "README")

