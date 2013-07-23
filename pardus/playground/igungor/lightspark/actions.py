#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure('-DCOMPILE_PLUGIN=1 \
                          -DPLUGIN_DIRECTORY="/usr/lib/browser-plugins" \
                          -DENABLE_SOUND=1 \
                          -DCMAKE_SKIP_RPATH=1 \
                          -DGNASH_EXE_PATH=/usr/bin/gnash')

def build():
    cmaketools.make()

def install():
    cmaketools.install()
