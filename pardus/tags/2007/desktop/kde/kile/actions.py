#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure()
    
def build():
    kde.make()
    
def install():
    kde.install()

    # fix #2999
    pisitools.remove("/usr/kde/3.5/share/apps/katepart/syntax/bibtex.xml")
    pisitools.remove("/usr/kde/3.5/share/apps/katepart/syntax/latex.xml")
