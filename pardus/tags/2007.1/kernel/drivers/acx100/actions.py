#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="acx-20070101"

def build():
    autotools.make("-C /lib/modules/%s/build M=`pwd`" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/net/wireless" % get.curKERNEL(), "*.ko")
    pisitools.dodoc("Changelog", "README")
