#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules

WorkDir = "bsddb3-4.4.2"

def install():
    pythonmodules.install("--berkeley-db=/usr")