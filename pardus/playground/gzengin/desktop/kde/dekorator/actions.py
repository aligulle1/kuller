#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    theme_dir = "%s/share/apps/deKorator/themes" % get.kdeDIR()
    pisitools.dodir(theme_dir)

    for theme in shelltools.ls("themesStuff/*-theme.tar.*"):
        shelltools.system("tar -xvf '%s' -C %s%s" % (theme, get.installDIR(), theme_dir))

    pisitools.dodoc("AUTHORS", "CHANGELOG", "README", "gpl.txt")