#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="tpm_emulator-0.5"

def build():
    autotools.make()

def install():
    pisitools.dosbin("tpmd/tpmd")
    pisitools.dolib("tddl/libtddl.so")
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "tpmd_dev/tpmd_dev.ko")
    pisitools.insinto("/usr/include","tddl/tddl.h")