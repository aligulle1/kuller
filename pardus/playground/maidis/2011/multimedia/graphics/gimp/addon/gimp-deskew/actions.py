#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gimp-plugins-ambulance-gimp-deskew-plugin"

def setup():
    autotools.autoreconf("-vif")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # very very thank you
    pisitools.domove("/usr/usr/lib/gimp/2.0/plug-ins/deskew", "/usr/lib/gimp/2.0/plug-ins")
    pisitools.removeDir("/usr/usr")

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "HACKING", "NEWS", "README", "TODO")
