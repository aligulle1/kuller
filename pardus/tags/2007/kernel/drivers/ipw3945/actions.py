#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def build():
    autotools.make("-C /lib/modules/%s/build M=`pwd` IEEE80211_API=2 EXTRA_CFLAGS=-DIEEE80211_API_VERSION=2" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/net/wireless" % get.curKERNEL(), "*.ko")
