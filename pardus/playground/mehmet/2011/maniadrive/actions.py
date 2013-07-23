#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get


#WorkDir = "ManiaDrive-%s-linux-i386" % get.srcVERSION()
data = "/usr/share/%s" % get.srcNAME()
NoStrip = "/"

#shelltools.export("CFLAGS", "%s" % get.CFLAGS())
#shelltools.export("CXXFLAGS", "%s" % get.CXXFLAGS())

def setup():
    pisitools.dosed("Makefile", "-L/usr/X11R6/lib/", "-L/usr/X11R6/lib/ -L/usr/lib/apache2/modules/")
    #autotools.configure()
    pass


def build():
    autotools.make("CFLAGS=\"%s -fPIC `php-config --includes`\" LDFLAGS=\"%s\" LINKING_OPTIONS=-Wl,-soname,libraydium-1.2.so" % (get.CFLAGS(), get.LDFLAGS()))


def install():
    pass
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 
    #pisitools.dodir("/usr/share")
    #shelltools.copytree("game", "%s%s" % (get.installDIR(), data))
    #pisitools.dodoc("README", "COPYING")

