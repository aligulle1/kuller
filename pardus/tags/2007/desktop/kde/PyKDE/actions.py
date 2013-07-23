#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pythonmodules.run("configure.py -d /usr/lib/%s/site-packages -v /usr/share/sip -c -k /usr/kde/3.5" % get.curPYTHON())

def build():
    autotools.make()

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README", "THANKS")

    pisitools.dodir("/usr/share/doc/PyKDE-%s-%s/html" % (get.srcVERSION(),get.srcRELEASE()))
    shelltools.copy("doc/*","%s/usr/share/doc/PyKDE-%s-%s/html" % (get.installDIR(),get.srcVERSION(),get.srcRELEASE()))
