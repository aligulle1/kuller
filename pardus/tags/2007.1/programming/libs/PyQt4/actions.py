#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "PyQt-x11-gpl-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("configure.py", "  check_license()", "# check_license()")

    pythonmodules.run("configure.py -q /usr/bin/qmake-qt4")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "LICENSE", "NEWS", "README", "README.Linux", "THANKS")

    pisitools.dodir("/usr/qt/4/doc/PyQt4")
    shelltools.copy("doc/html/*","%s/usr/qt/4/doc/PyQt4" % get.installDIR())
    pisitools.dosym("/usr/qt/4/doc/PyQt4/classes.html","/usr/qt/4/doc/PyQt4/index.html")
