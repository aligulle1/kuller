#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-ipv6 \
                         --disable-smb \
                         --mandir=/usr/share/man")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("CHANGES", "LICENSE", "README")
