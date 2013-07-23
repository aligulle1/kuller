#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--enable-gc=system")

def build():
    autotools.make()

    # generate FAQ html
    shelltools.cd("doc/FAQ")
    autotools.make()

def install():
    pisitools.dobin("asy")
    pisitools.insinto("/usr/share/asymptote","base/*.asy")

    for examplesdata in ["examples/*.asy","examples/animations","doc/*.asy","doc/*.csv", "doc/*.dat", "doc/*.tex","doc/extra/*"]:
        pisitools.insinto("/usr/share/doc/asymptote/examples",examplesdata)

    # remove unneeded files
    pisitools.remove("/usr/share/doc/asymptote/examples/animations/dice.u3d")
    pisitools.remove("/usr/share/doc/asymptote/examples/intro_.bbl")
    pisitools.remove("/usr/share/doc/asymptote/examples/CAD.tex")

    # add FAQ and man
    pisitools.insinto("/usr/share/doc/asymptote","doc/FAQ/asy-faq.html")
    pisitools.insinto("/usr/share/doc/asymptote","doc/FAQ/asy-faq.ascii")
    pisitools.doman("doc/asy.1")

    # add needed sty 
    pisitools.insinto("/usr/share/texmf-dist/tex/latex/asymptote","doc/*.sty")

    # add files for emacs users and vim users
    for data in ["asy-keywords.el","base/asy-init.el","base/asy-mode.el"]:
        pisitools.insinto("/usr/share/emacs/site-lisp",data)

    pisitools.insinto("/usr/share/vim/vim71/asy/","base/*.vim")

    # add python interpreter example for asymptote
    pisitools.insinto("/usr/lib/%s/site-packages/" % get.curPYTHON(),"base/*.py")
