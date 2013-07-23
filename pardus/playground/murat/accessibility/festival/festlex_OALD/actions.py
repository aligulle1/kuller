#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "festival/lib/dicts/oald"

def install():
    for files in ["*.scm", "oald-0.4.out"]:
        pisitools.insinto("/usr/share/festival/dicts/oald", files)

    shelltools.system("tar xvfz oald2ft.tar.gz")
    shelltools.cd("oald2ft")
    autotools.make()
    pisitools.dobin("oald2ft")
    shelltools.cd("..")

    pisitools.dodoc("COPYING", "README.oald")
