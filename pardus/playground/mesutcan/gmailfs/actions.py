#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
     pisitools.dobin("gmailfs.py")
     shelltools.chmod("gmailfs.conf", 0644)
     pisitools.dodir("/etc/gmailfs")
     pisitools.insinto("/etc/gmailfs/", "gmailfs.conf")

