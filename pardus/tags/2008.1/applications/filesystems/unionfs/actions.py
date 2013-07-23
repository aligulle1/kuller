#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools

WorkDir = "unionfs_utils-0.2.1"

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
