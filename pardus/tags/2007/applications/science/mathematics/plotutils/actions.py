#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # May have trouble with cpu flags
    autotools.configure("--with-x \
                        --enable-libxmi \
                        --enable-libplotter")
                        
def build():
    autotools.make()

def install():
    autotools.install("datadir=%s/usr/share" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COMPAT", "ChangeLog", "INSTALL*", "KNOWN_BUGS", "NEWS", "ONEWS", "PROBLEMS", "README", "THANKS", "TODO")

    #FIXME: we are not installing the ps fonts now, we should check if it breaks ghostscrip and printers
    #       read INSTALL.fonts for more info
