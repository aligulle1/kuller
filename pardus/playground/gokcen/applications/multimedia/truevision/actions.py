#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from glob import glob

WorkDir="truevision-0.5.5"

def setup():
    #FIXME get installed povray dir normally
    povrayDir = glob("/usr/share/povray-*")[0]
    pisitools.dosed("src/preferences.cc", "/usr/lib/povray", povrayDir)
    pisitools.dosed("src/preferences.cc", "povcmd->set\( \"povray\"", "povcmd->set( \"/usr/bin/povray\"")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

