# -*- coding: utf-8 -*-
#
# Copyright 2012 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "StarBoardSoftware9.31_Linux-111118/StarBoardSoftware_9.31"

def setup():
    pisitools.dosed('install.sh', r'(^MOVE\s*=.*)', '\\1\n\nDESTDIR=%s' % get.installDIR())
    pisitools.dosed('data/usr/local/StarBoardSoftware/install.sh', r'(#!/bin/sh)', '\\1\n\nexport DESTDIR="%s"' % get.installDIR())

def install():
    shelltools.system("./install.sh")
