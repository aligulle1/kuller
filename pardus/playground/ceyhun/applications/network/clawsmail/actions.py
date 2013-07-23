#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "claws-mail-3.7.0"

def setup():
    autotools.rawConfigure('--disable-libetpan')

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README", "ChangeLog", "COPYING", "AUTHORS", "NEWS", "TODO")
