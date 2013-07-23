#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "festival/lib/dicts"

def install():
    for files in ["wsj.wp39.poslexR", "wsj.wp39.tri.ngrambin"]:
        pisitools.insinto("/usr/share/festival/dicts", files)

    pisitools.dodoc("COPYING.poslex")
