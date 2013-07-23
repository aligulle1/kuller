#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "PyQt-x11-gpl-3.17"

def setup():
    pisitools.dosed("configure.py", "  check_license()", "# check_license()")

    pythonmodules.run("configure.py \
                       -d /usr/lib/%s/site-packages \
                       -b /usr/bin \
                       -v /usr/share/sip" % get.curPYTHON())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/PyQt.html")
    pisitools.dodoc("ChangeLog", "LICENSE", "NEWS", "README", "README.Linux", "THANKS")
