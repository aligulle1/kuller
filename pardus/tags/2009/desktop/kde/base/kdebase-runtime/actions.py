#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os
import gzip

NoStrip = ["/usr/kde/4/share/", "/usr/share"]

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DICON_INSTALL_DIR=\"/usr/share/icons\"", installPrefix="/usr/kde/4", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def mygunzip(_file):
    r_file = gzip.GzipFile(_file, "r")
    write_file = _file.replace(".svgz", ".svg")
    w_file = open(write_file, "w")
    w_file.write(r_file.read())
    w_file.close()
    r_file.close()
    os.unlink(_file)

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #delete kmplayer icons from oxygen theme
    prefix = "/usr/share/icons/oxygen/"
    conflictingIcons = ("kmplayer", "digikam", "showfoto")

    for size in (16, 22, 32, 48, 64, 128):
        for icon in conflictingIcons:
            pisitools.remove("%s%sx%s/apps/%s.png" % (prefix, size, size, icon))

    for icon in conflictingIcons:
        pisitools.remove("%sscalable/apps/%s.svgz" % (prefix, icon))

    #Unzip svgz icons to better compress them with lzma (in install.tar.lzma)
    for root, dirs, files in os.walk("%s/%s/scalable" % (get.installDIR(), prefix)):
        for name in files:
            if name.endswith(".svgz"):
                f = os.path.join(root, name)
                mygunzip(f)

    #remove index.theme file of hicolor icon theme, correct source for the file is the hicolor icon theme package itself
    pisitools.remove("/usr/share/icons/hicolor/index.theme")

