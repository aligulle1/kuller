#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "backintime-%s" % get.srcVERSION()

def setup():
    shelltools.cd("common") 
    autotools.configure()

def build():
    shelltools.cd("common")
    autotools.make()

def install():
    pisitools.dodoc("AUTHORS", "CHANGES", "LICENSE", "TODO", "README", "VERSION", "TRANSLATIONS")  
  
    shelltools.cd("common")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
