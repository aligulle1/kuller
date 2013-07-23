#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "."

def install():
    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME, "gpl-2.0.txt", "COPYING")