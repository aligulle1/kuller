#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir = "kmhtconvert-0.7.3"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "LICENSE")
