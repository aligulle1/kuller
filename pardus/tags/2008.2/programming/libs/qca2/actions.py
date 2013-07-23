#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = 'qca-%s' % (get.srcVERSION())

def setup():
    autotools.rawConfigure("--prefix=/usr/qt/4 --qtdir=/usr/qt/4 --datadir=/usr/share")

def build():
    autotools.make()
    autotools.make("apidox")

def install():
    # Remove source build directory variable
    pisitools.dosed("lib/libqca.prl", "QMAKE_PRL_BUILD_DIR = %s/qca-%s/src" % (get.workDIR(), get.srcVERSION()), "")

    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    # Put apidocs in its own directory
    pisitools.dodir("/usr/share/doc/qca2-apidocs/html")
    pisitools.insinto("/usr/share/doc/qca2-apidocs/html", "apidocs/html/*")

    pisitools.domove("/usr/qt/4/lib/pkgconfig/qca2.pc", "/usr/lib/pkgconfig")

    pisitools.dodoc("README", "TODO", "COPYING")
