#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "festival/lib/dicts/cmu"

def install():
    for files in ["*.scm", "cmu2ft", "cmudict-0.4.out"]:
        pisitools.insinto("/usr/share/festival/dicts/cmu", files)

    pisitools.dodoc("COPYING")
