#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "links-2.1pre20"

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.cd("intl")
    shelltools.system("./gen-intl")
    shelltools.cd("..")
    
    autotools.configure("--without-x \
                         --without-svgalib \
                         --without-sdl \
                         --without-pmshell \
                         --without-atheos \
                         --with-ssl \
                         --enable-graphics")
    
def build():
    autotools.make()
    
def install():
    shelltools.export("LC_ALL", "C")
    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("links", "/usr/bin/links2")
    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "SITES", "TODO")        
