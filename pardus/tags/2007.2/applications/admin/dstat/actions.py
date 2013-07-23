#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

def install():
    pisitools.dobin("dstat")

    pisitools.insinto("/usr/share/dstat", "plugins/*.py")
    pisitools.doman("dstat.1")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "TODO", "dstat.conf", "examples/mstat.py", "examples/read.py")
