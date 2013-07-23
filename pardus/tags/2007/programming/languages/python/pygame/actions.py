#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "pygame-%srelease" % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodir(get.docDIR())
    shelltools.copytree("docs", "%s/%s/%s" % (get.installDIR(), get.docDIR(), get.srcTAG()))
    shelltools.copytree("examples", "%s/%s/%s/" % (get.installDIR(), get.docDIR(), get.srcTAG()))

