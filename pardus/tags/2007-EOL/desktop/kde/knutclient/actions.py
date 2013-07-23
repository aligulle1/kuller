#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde


def setup():
    # admin folder has problems, so we workaround
    shelltools.unlink("configure")
    autotools.autoconf()
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    # we use our desktop file
    pisitools.remove("%s/share/applications/kde/knutclient.desktop" % get.kdeDIR())

