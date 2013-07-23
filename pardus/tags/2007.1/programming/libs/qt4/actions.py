#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

WorkDir = "qt-x11-opensource-src-%s" % get.srcVERSION()

qtbase = "/usr/qt/4"

def setup():
    autotools.rawConfigure("-pch \
                            -stl \
                            -fast \
                            -prefix %s \
                            -libdir %s/lib \
                            -qt-gif \
                            -qdbus \
                            -glib \
                            -system-sqlite \
                            -plugin-sql-sqlite \
                            -plugin-sql-mysql \
                            -plugin-sql-pgsql \
                            -I/usr/include/mysql \
                            -I/usr/include/postgresql/server/ \
                            -release \
                            -no-separate-debug-info \
                            -no-exceptions \
                            -confirm-license " % (qtbase, qtbase))

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.dodir("/usr/bin")

    for app in ["qmake","designer","assistant","linguist","qtconfig","uic","rcc","moc","lrelease","lupdate"]:
        pisitools.dosym("/usr/qt/4/bin/%s" % app,"/usr/bin/%s-qt4" % app)

    for app in ["qdbus","qdbuscpp2xml","qdbusxml2cpp","qt3to4","qtdemo","uic3","pixeltool"]:
        pisitools.dosym("/usr/qt/4/bin/%s" % app,"/usr/bin/%s" % app)

    pisitools.insinto("/usr/lib/pkgconfig","%s/usr/qt/4/lib/*.pc" % get.installDIR())
    pisitools.dosed("%s/usr/lib/pkgconfig/*.pc" % get.installDIR(), "%s/qt-x11-opensource-src-%s" % (get.workDIR(),get.srcVERSION()),"/usr/qt/4")
    pisitools.remove("/usr/qt/4/lib/*.pc")

    for root, dirs, files in os.walk("."):
        for name in files:
            if name.endswith(".prl"):
                pisitools.dosed(name, "%s/qt-x11-opensource-src-%s" % (get.workDIR(),get.srcVERSION()),"/usr/qt/4")
