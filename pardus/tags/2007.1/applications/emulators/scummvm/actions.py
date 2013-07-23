#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    ''' Must '''
    autotools.rawConfigure("--prefix=%s/usr --enable-lure --enable-cine --enable-agi" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.install()
