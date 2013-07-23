#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

WorkDir = "qt-x11-opensource-src-%s" % get.srcVERSION()
qtbase = "/usr/qt/4"

def setup():
    # phonon module is disabled because, it's been packaged from KDE SVN repository to compile KDE 4.1 packages
    autotools.rawConfigure("-no-pch \
                            -v \
                            -stl \
                            -fast \
                            -prefix %s \
                            -libdir %s/lib \
                            -qdbus \
                            -qvfb \
                            -glib \
                            -no-sql-sqlite2 \
                            -system-sqlite \
                            -plugin-sql-sqlite \
                            -plugin-sql-mysql \
                            -plugin-sql-psql \
                            -I/usr/include/mysql \
                            -I/usr/include/postgresql/server/ \
                            -release \
                            -no-separate-debug-info \
                            -no-exceptions \
                            -no-phonon \
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

    # Turkish translations
    shelltools.system("%s/usr/qt/4/bin/lrelease l10n-tr/*.ts" % get.installDIR())
    pisitools.insinto("/usr/qt/4/translations","l10n-tr/*.qm")

    pisitools.insinto("/usr/lib/pkgconfig","%s/usr/qt/4/lib/pkgconfig/*.pc" % get.installDIR())
    pisitools.dosed("%s/usr/lib/pkgconfig/*.pc" % get.installDIR(), "%s/qt-x11-opensource-src-%s" % (get.workDIR(),get.srcVERSION()),"/usr/qt/4")
    pisitools.remove("/usr/qt/4/lib/pkgconfig")

    for root, dirs, files in os.walk("%s/usr/qt/4" % get.installDIR()):
        for name in files:
            if name.endswith(".prl"):
                pisitools.dosed(os.path.join(root, name),"%s/qt-x11-opensource-src-%s" % (get.workDIR(),get.srcVERSION()),"/usr/qt/4")
