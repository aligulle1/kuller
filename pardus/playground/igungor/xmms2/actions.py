#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

shelltools.export("JOBS", os.environ["JOBS"].replace("-j", ""))
shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("./waf configure \
                             --prefix=/usr \
                             --without-ldconfig \
                             --nocache")

def build():
    shelltools.system("./waf build")

def install():
    shelltools.system("./waf install --destdir=%s" % get.installDIR())

