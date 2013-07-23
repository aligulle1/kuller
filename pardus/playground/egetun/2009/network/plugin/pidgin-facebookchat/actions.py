#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "/usr"
files = {"lib/purple-2/libfacebook.so": "/usr/lib/purple-2",
         "lib/pidgin/libfacebookarm.so": "/usr/lib/pidgin",
         "share": "/usr/"}

def install():
    for i in files:
        pisitools.insinto(files[i], i)

