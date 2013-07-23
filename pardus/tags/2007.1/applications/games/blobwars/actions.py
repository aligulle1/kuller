#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('DATADIR=/%s/blobwars/ DOCDIR=/%s/%s/' % (get.dataDIR(), get.docDIR(), get.srcTAG()))
    # if you want the map editor, comment out
    #autotools.make('mapeditor')

def install():
    autotools.rawInstall('DESTDIR=%s \
                          BINDIR=%s/usr/bin/ \
                          DATADIR=%s/%s/blobwars/ \
                          DOCDIR=%s/%s/%s/' % (get.installDIR(), get.installDIR(), get.installDIR(), get.dataDIR(), 
			  get.installDIR(), get.docDIR(), get.srcTAG()))
    # if you want the map editor, comment out
    pisitools.insinto('/usr/bin/', 'mapeditor', '/usr/bin/blobwars-mapeditor')
    
    pisitools.removeDir('/usr/share/icons/large')
    pisitools.removeDir('/usr/share/icons/mini')
