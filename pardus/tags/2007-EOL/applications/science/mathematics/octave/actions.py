#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("WANT_AUTOCONF","2.59")

    autotools.autoconf()
    autotools.configure()
    
def build():
    autotools.make()
    
def install():
    autotools.install()

    pisitools.dosed("%s/usr/libexec/octave/*/oct/*/PKG_ADD" % get.installDIR(), "%s" % get.installDIR(), "")
