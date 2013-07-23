#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import get

def build():
    scons.make("target=radiant,q3map2 config=debug")
    #shelltools.system("doxygen")

def install():

    shelltools.copytree("install/", "%s/opt/ZeroRadiant/" % get.installDIR())

    pisitools.dodoc("BSD", "COMPILING", "CONTRIBUTORS", "CONTRIBUTOR_AGREEMENT", "ChangeLog", "GPL", "LGPL", "LICENSE", "README", "TODO", "TRANSLATING")
