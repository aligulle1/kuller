#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure("--enable-gc=system")

def build():
    autotools.make()

def install():
    pisitools.dobin("asy")
    pisitools.insinto("/usr/share/asymptote/","base/*.asy")
    pisitools.insinto("/usr/share/doc/asymptote-%s-%s/examples" % (get.srcVERSION(),get.srcRELEASE()),"examples/*")
    pisitools.insinto("/usr/share/texmf-dist/tex/latex/asymptote","doc/*.sty")
    pisitools.doman("doc/asy.1")
