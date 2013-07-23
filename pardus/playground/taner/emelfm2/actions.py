#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = 'avidemux_%s' % get.srcVERSION()

def build():
    autotools.make()

def install():
    autotools.rawInstall("PREFIX=%s/usr/" % get.installDIR())
    autotools.rawInstall("PREFIX=%s/usr/ install_i18n" % get.installDIR())
    pisitools.remove("/usr/share/applications/emelfm2.desktop")
