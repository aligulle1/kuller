#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

data = ["obextool.tk","plugins","lib","lang","images"]
datadir = "/usr/share/obextool"

def install():
    pisitools.dobin("contrib/startup/obextool")

    pisitools.insinto("/etc/obextool","etc/*")

    for files in data:
          pisitools.insinto(datadir,files)

    pisitools.dodoc("doc/ChangeLog","doc/COPYING","doc/TODO")
