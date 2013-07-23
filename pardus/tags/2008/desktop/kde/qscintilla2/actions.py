#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "QScintilla-gpl-2.2"
Qt4DIR = "usr/qt/4"
qmake = "qmake-qt4"

def setup():
    shelltools.cd("Qt4/")

    pisitools.dosed("qscintilla.pro", "DESTDIR = \$\(QTDIR\)/lib", "DESTDIR = %s/%s/lib" % (get.installDIR(), Qt4DIR))
    pisitools.dosed("qscintilla.pro", "DESTDIR = \$\$\[QT_INSTALL_LIBS\]", "DESTDIR = %s/%s/lib" % (get.installDIR(), Qt4DIR))
    shelltools.system("%s -o Makefile qscintilla.pro" % qmake)

    # Change C/XXFLAGS
    pisitools.dosed("Makefile", "^CFLAGS   = -pipe -w -mcpu=i686 -O2 -pipe", "CFLAGS   = %s -w" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS = -pipe -w -mcpu=i686 -O2 -pipe", "CXXFLAGS = %s -w" % get.CXXFLAGS())

    # Get designer plugin's Makefile
    shelltools.cd("../designer-Qt4/")
    pisitools.dosed("designer.pro", "-L\.\./Qt4/lib", "-L%s/%s/lib" % (get.installDIR(), Qt4DIR))
    shelltools.system("%s -o Makefile designer.pro" % qmake)

    # Change C/XXFLAGS of designer plugin's makefile
    pisitools.dosed("Makefile", "^CFLAGS   = -pipe -w -mcpu=i686 -O2 -pipe", "CFLAGS   = %s -w" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS = -pipe -w -mcpu=i686 -O2 -pipe", "CXXFLAGS = %s -w" % get.CXXFLAGS())

def install():

    # execute install target of build system
    shelltools.cd("Qt4/")
    autotools.make("all staticlib CC=\"%s\" CXX=\"%s\" LINK=\"%s\"" % (get.CC(), get.CXX(), get.CC()))
    pisitools.insinto("/%s/lib" % Qt4DIR, "libqscintilla2.so*")

    shelltools.cd("../designer-Qt4/")
    autotools.make("DESTDIR=\"%s/%s/plugins/designer\"" % (get.installDIR(), Qt4DIR))

    # Get Makefile of qscintilla-python via sip
    shelltools.cd("../Python")
    pythonmodules.run("configure.py -p 4 -n ../Qt4 -o ../Qt4")

    # installs not managed by the build system
    shelltools.cd("../Qt4/")
    shelltools.makedirs("%s/%s/include" % (get.installDIR(), Qt4DIR))
    shelltools.copytree("Qsci", "%s/%s/include/Qsci" % (get.installDIR(), Qt4DIR))
    pisitools.insinto("%s/translations" % Qt4DIR, "qscintilla*.qm")

    shelltools.cd("../")
    pisitools.insinto("%s/plugins/designer" % Qt4DIR, "designer-Qt4/libqscintillaplugin.so")

    #build and install qscintilla-python
    shelltools.cd("Python")
    autotools.make()
    autotools.install("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dohtml("doc/html-Qt4/")
    pisitools.insinto("/usr/share/doc/%s/Scintilla" % get.srcTAG(), "doc/Scintilla/*")

    pisitools.dodoc("ChangeLog", "LICENSE", "NEWS", "README")
