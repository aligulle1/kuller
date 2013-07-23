#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "."
NoStrip = "/"

def install():

#   Patch download 

#   ftp://expdownload:dudummerpiratleecher@ftp2.extreme-players.de/Games/et/mods/truecombat/tcetest_0.48_update.zip
#   ftp://ftp:HGmf563@floze.de/filebase/Games/et/mods/truecombat/tcetest_0.48_update.zip
#   http://server12.download.filefront.com/rsuqhphrzn+/gamingfiles/Wolfenstein_Enemy_Territory/Mods/tcetest_0.48_update.zip
#   ftp://ftp.games.skynet.be/pub/www.filesnetwork.com/Wolfenstein_Enemy_Territory/Mods/Total_Conversions/tcetest_0.48_update.zip
#   http://downloads.planetmirror.com/pub/filesnetwork/Wolfenstein_Enemy_Territory/Mods/Total_Conversions/tcetest_0.48_update.zip


    shelltools.system("echo downloading Patch 0.48")
    shelltools.system("wget -c ftp://expdownload:dudummerpiratleecher@ftp2.extreme-players.de/Games/et/mods/truecombat/tcetest_0.48_update.zip")
    shelltools.system("unzip -o tcetest_0.48_update.zip")

    shelltools.cd("tcetest")   
    pisitools.insinto("/opt/enemy-territory/tcetest", "*")
    pisitools.dodoc("*.txt")
