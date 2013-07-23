#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="sisctrl-0.0.20051202"

def setup():
    autotools.configure("--with-xv-path=/usr/lib")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS","ChangeLog","NEWS","README")
    pisitools.insinto("/usr/share/","icons")
    pisitools.insinto("/usr/share/applications","extra/sisctrl.desktop")
