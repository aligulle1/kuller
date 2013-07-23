#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--docdir=/usr/share/doc/pdfedit-%s" % get.srcVERSION())

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "%s/usr/share/pdfedit/icon/pdfedit_logo.png" % get.installDIR(), "pdfedit.png")
    #autotools.install()

    #shelltools.makedirs("%s/usr/share/pdfedit" % get.installDIR())
    #for files in shelltools.ls("%s/usr/share/*.qs" % get.installDIR()):
    #        shelltools.move(files, "%s/usr/share/pdfedit" % get.installDIR())

    #for files in ["pdfeditrc", "mode.conf", "operator.hint"]:
    #    shelltools.move("%s/usr/share/%s" % (get.installDIR(), files), "%s/usr/share/pdfedit/" % get.installDIR())


    #for dir in ["lang", "scripts", "icon", "help"]:
    #    shelltools.copytree("%s/usr/share/%s" % (get.installDIR(), dir), "%s/usr/share/%s/" % (get.installDIR(), get.srcNAME()))
    #    shelltools.unlinkDir("%s/usr/share/%s" % (get.installDIR(), dir))


    #pisitools.dodoc("COPYING", "README", "Changelog")
    #for i in shelltools.ls("%s/usr/share/doc/pdfedit/*" % get.installDIR()):
    #    shelltools.move(i, "%s/usr/share/doc/%s" % (get.installDIR(), get.srcTAG()))
    #shelltools.unlinkDir("%s/usr/share/doc/pdfedit/" % get.installDIR())
