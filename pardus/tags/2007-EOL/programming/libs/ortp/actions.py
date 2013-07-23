#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-ipv6 \
                         --disable-static \
                         --enable-debug=no")
    
def build():
    autotools.make()
    
def install():
    autotools.install()
    
    pisitools.dodoc("README","ChangeLog","NEWS","COPYING","AUTHORS","TODO")
    pisitools.dohtml("%s/usr/share/gtk-doc/html/ortp/*" % get.installDIR())
    pisitools.removeDir("/usr/share/gtk-doc")
