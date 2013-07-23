#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde

def setup():
    # needed by networkstatus.patch
    kde.make("-f admin/Makefile.common")
    kde.configure("--disable-final")

def build():
    kde.make()

def install():
    kde.install()
