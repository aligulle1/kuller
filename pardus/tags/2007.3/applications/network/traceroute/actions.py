#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    pisitools.doexe("traceroute/traceroute", "/bin/")
    pisitools.dosym("/bin/traceroute", "/bin/tracert")
    pisitools.doman("traceroute.8")
    pisitools.dodoc("ChangeLog", "COPYING", "CREDITS", "README", "TODO")
