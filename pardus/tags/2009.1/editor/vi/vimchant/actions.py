#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    try:
        vimDir = shelltools.ls("/usr/share/vim/*")[0]
    except IndexError:
        vimDir = "/usr/share/vim/vim72"

    pisitools.insinto("%s/autoload" % vimDir, "autoload/*")
    pisitools.insinto("%s/plugin" % vimDir, "plugin/*")

    pisitools.dodoc("doc/*.txt")
