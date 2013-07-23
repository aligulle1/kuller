#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    pisitools.domo("po/tr.po", "tr", "kdenlive.mo")
    pisitools.domove("/usr/share/locale/tr", "%s/share/locale/tr" % get.kdeDIR())