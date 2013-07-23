#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

def install():
    autotools.rawInstall("BINDIR=%s/usr/bin DESTDIR=%s/usr/share/sgml/docbook/dsssl-stylesheets-%s install" 
                         % (get.installDIR(),get.installDIR(),get.srcVERSION()))
