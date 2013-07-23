#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Fahri Tuğrul Gürkaynak <ftugrul@gmail.com>

from pisi.actionsapi import autotools

def setup():
    autotools.configure("--disable-scrollkeeper")

def build():
    autotools.make()

def install():
    autotools.install()
