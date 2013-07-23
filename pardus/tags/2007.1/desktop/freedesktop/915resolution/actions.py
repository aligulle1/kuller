#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def build():
    autotools.make("clean")
    autotools.make('CFLAGS="%s"' % get.CFLAGS())

def install():
    pisitools.dosbin("915resolution")
    pisitools.dodoc("README.txt", "LICENSE.txt", "changes.log", "chipset_info.txt", "dump_bios")
 
