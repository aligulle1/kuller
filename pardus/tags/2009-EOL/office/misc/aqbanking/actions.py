#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

# Use Qt4 instead of Qt3
QTDIR = get.qtDIR()
QTINC = "%s/include" % QTDIR
QTINCPATH = " ".join(["-I%s/%s" % (QTINC, p) for p in ("", "Qt", "QtCore", "QtGui", "Qt3Support")])
QTLIBS = "-L%s/lib -lQtCore -lQtGui -lQt3Support" % QTDIR


def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-qt3 \
                         --disable-aqfinance \
                         --enable-gwenhywfar \
                         QTDIR=\"%s\" qt3_libs=\"%s\" qt3_includes=\"%s\"" % (QTDIR, QTLIBS, QTINCPATH))


def build():
    autotools.make("-j1 qt4-port")
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/aqhbci")
