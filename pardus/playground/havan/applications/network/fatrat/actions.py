#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

#WorkDir = "fatrat-1.0_rc1"

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.install("DESTDIR=%s" % get.installDIR())

