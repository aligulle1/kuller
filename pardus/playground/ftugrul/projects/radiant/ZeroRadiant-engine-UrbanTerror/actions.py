#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

from os import walk

WorkDir = "."

def setup():
    shelltools.cd("UrbanTerror/q3ut4/")
    shelltools.system("unzip zpak000_assets.pk3")
    shelltools.system("unzip zpak000.pk3")

    for files in walk("%s/opt/ZeroRadiant/engine-UrbanTerror/q3ut4/maps/" % get.workDIR()):
        shelltools.unlink("%s/opt/ZeroRadiant/engine-UrbanTerror/q3ut4/maps/%s" % (get.workDIR(), files))

    for pk3 in ["zpak000_assets", "zpak000"]:
        shelltools.unlink("%s/UrbanTerror/q3ut4/%s.pk3" % (get.workDIR(), pk3))

def install():
    destination = "%s/opt/ZeroRadiant/engine-UrbanTerror/" % get.installDIR()

    shelltools.copytree("UrbanTerror/", destination)
    shelltools.chmod("%s/ioUrbanTerror.i386" % destination, 0755)

