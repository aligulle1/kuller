#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde4

shelltools.export("HOME", get.workDIR())
NoStrip=["/usr/share"]

def setup():
    kde4.configure("-DBUILD_kdeaccounts-plugin=NO")

def build():
    kde4.make()

def install():
    kde4.install()

    # those come from subversion package
    for f in ["svnrevertlast", "svnlastchange", "svnlastlog"]:
        pisitools.remove("/usr/bin/%s" % f)
    # there are no binaries for these manpages
    pisitools.remove("/usr/share/man/man1/transxx.1")
    pisitools.remove("/usr/share/man/man1/reportview.1")
    
    pisitools.dodoc("README", "COPYING*")