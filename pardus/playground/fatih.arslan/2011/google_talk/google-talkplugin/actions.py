#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def install():
    pisitools.dodir("/opt/google/talkplugin")
    shelltools.copy("%s/%s/*" % (get.workDIR(), get.srcDIR()), "%s/opt/google/talkplugin" % get.installDIR())

    pisitools.dosym("/opt/google/talkplugin/libnpgoogletalk64.so", "/usr/lib/browser-plugins/libnpgoogletalk64.so")
    pisitools.dosym("/opt/google/talkplugin/libnpgtpo3dautoplugin.so", "/usr/lib/browser-plugins/libnpgtpo3dautoplugin.so")
