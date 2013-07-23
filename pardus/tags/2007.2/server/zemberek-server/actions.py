#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="zemberek-server"

def build():
    shelltools.system("ant dist")

def install():
    shelltools.cd("dist/")
    pisitools.insinto("/opt/zemberek-server/config", "config/*")
    pisitools.insinto("/opt/zemberek-server/lib", "lib/*")
    pisitools.insinto("/opt/zemberek-server/lisanslar", "lisanslar/*")
    pisitools.insinto("/opt/zemberek-server", "zemberek_server-0.7.jar")
    pisitools.insinto("/opt/zemberek-server", "run*.sh")
    pisitools.insinto("/etc/dbus-1/system.d", "config/zemberek-server.conf")