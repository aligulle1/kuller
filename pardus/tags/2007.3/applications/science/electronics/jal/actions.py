#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "jal"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "MAINTAINERS", "NEWS", "PIC18_news.txt", "README", "TODO", "doc/jal.doc", "doc/*.jal", "doc/*.tcl")
    pisitools.dohtml("doc/*.html")
