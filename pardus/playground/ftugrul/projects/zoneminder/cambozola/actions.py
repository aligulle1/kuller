#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2008  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import pisitools
import os

def install():
    os.system("ant")
    pisitools.insinto("/opt/cambozola", "dist/*")
    pisitools.dodoc("LICENSE", "README*")