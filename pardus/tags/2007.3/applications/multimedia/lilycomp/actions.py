#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = "lilycomp.1.0.2"

def install():
    pisitools.dobin("lilycomp.py")
    pisitools.rename("/usr/bin/lilycomp.py", "lilycomp")
    pisitools.dohtml("*.html")
    pisitools.dodoc("CHANGES", "COPYRIGHT", "LICENSE")
