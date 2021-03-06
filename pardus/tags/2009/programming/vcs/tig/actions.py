#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CC", get.CC())
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    autotools.install(argument="install-doc-man")

    pisitools.insinto("/etc/bash_completion.d", "contrib/tig-completion.bash", "tig")

    pisitools.dodoc("BUGS", "COPYING", "NEWS", "README", "SITES", "TODO", "manual.txt", "contrib/tigrc")
    pisitools.dohtml("*.html")
