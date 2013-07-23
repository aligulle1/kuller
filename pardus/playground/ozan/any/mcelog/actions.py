#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def build():
    autotools.make("CFLAGS=\"%s -fpie -pie\"" % get.CFLAGS())

def install():
    pisitools.doman("mcelog.8")
    pisitools.dosbin("mcelog")

    pisitools.insinto("/etc/mcelog/triggers", "triggers/*")
    pisitools.insinto("/etc/logrotate.d", "*logrotate")

    pisitools.dodoc("README")
