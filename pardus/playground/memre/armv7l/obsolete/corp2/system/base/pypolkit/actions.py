#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

#from pisi.actionsapi import pythonmodules
from pisi.actionsapi import crosstools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

def build():
    crosstools.prepare()

    links = ""
    for pc in ["gio-2.0", "gobject-2.0", "gmodule-2.0", "gthread-2.0", "glib-2.0"]:
        p = os.popen("pkg-config --libs %s" % pc)
        links += " %s" % p.readline().strip()

    crosstools.environment["CFLAGS"] = "%(CFLAGS)s \
                                        -I%(RootDir)s/usr/include/python2.6 \
                                        -I%(RootDir)s/usr/include/polkit-1 \
                                        -I%(RootDir)s/usr/include/glib-2.0 \
                                        -I%(RootDir)s/usr/lib/glib-2.0/include \
                                        -g3 -ggdb -fPIC" % crosstools.environment

    crosstools.environment["source"] = 'pypolkit'
    crosstools.environment["links"] = links

    shelltools.system("%(CC)s %(CFLAGS)s -c %(source)s.c -o %(source)s.o" % crosstools.environment)
    shelltools.system("%(CC)s -shared %(CFLAGS)s %(LDFLAGS)s %(source)s.o \
                       -lpython2.6 %(links)s -o _polkit.so" % crosstools.environment)

def install():
    #pythonmodules.install()

    shelltools.makedirs("%s/usr/lib/python2.6/site-packages/" % get.installDIR())
    shelltools.copy("*so", "%s/usr/lib/python2.6/site-packages/" % get.installDIR())
    shelltools.copy("polkit.py", "%s/usr/lib/python2.6/site-packages/" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "PKG-INFO", "README")
