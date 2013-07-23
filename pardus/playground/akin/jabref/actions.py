#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

NoStrip="/"

def setup():
    shelltools.system("ant")

def install():

    shelltools.cd("build")

    for directory in ["classes","help","images","lib","resource"]:
        pisitools.insinto("/usr/lib/jabref",directory)

