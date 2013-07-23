# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    for dir in ["base","extensions","themes"]:
        pisitools.insinto("/usr/share/texmf-dist/tex/latex/beamer",dir)

    pisitools.insinto("/usr/share/texmf-dist/tex/latex/beamer/emulation", "emulation/*.sty")

    pisitools.dodoc("README","ChangeLog","doc/licenses/LICENSE", "AUTHORS")
    pisitools.insinto("/usr/share/doc/%s/doc" % get.srcNAME(), "doc/*")

    for dir in ["examples", "emulation/examples", "solutions"]:
        pisitools.insinto("/usr/share/doc/%s/" % get.srcNAME(), dir)

    rms= []
    for i in ["*.tex~","._beamerexample-lecture-pic*"]:
        rms.extend(shelltools.ls(i))
    for rm in rms:
        pisitools.remove("examples/a-lecture/%s" % rms)
