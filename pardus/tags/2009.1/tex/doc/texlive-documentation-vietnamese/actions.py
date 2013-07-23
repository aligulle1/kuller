#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import texlivemodules

WorkDir="texlive-documentation-viatnamese-20080816"

def build():
    texlivemodules.compile()

def install():
    texlivemodules.install()

