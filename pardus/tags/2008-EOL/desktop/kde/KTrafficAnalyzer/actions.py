#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "KTrafficAnalyzer-0.3.9-1"

def build():
    kde.make()

def install():
    pisitools.insinto("%s/bin/" % get.kdeDIR(), "KTrafficAnalyzer")
