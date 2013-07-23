#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import kde

def setup():
    kde.make("-f admin/Makefile.common cvs")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
    pisitools.domove("%s/share/apps/kompose/icons" % get.kdeDIR(), "%s/share" % get.kdeDIR())
