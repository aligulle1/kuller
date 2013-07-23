#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    pisitools.insinto("/usr/share/gmailfs/", "gmailfs.py")
    pisitools.dobin("mount.gmailfs")

    shelltools.chmod("gmailfs.conf",0600)
    pisitools.insinto("/etc", "gmailfs.conf")

    pisitools.dodoc("ChangeLog","COPYING")
