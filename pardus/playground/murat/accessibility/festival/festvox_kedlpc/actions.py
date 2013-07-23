#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "festival/lib/voices/english/ked_diphone"

def install():
    pisitools.insinto("/usr/share/festival/voices/english/ked_diphone/festvox", "festvox/*")
    pisitools.insinto("/usr/share/festival/voices/english/ked_diphone/group", "group/*")

    pisitools.dodoc("COPYING")
