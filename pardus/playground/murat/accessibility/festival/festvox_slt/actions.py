#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "festival/lib/voices/us/cmu_us_slt_arctic_hts"

def install():
    pisitools.insinto("/usr/share/festival/voices/us/cmu_us_slt_arctic_hts/festvox", "festvox/*")
    pisitools.insinto("/usr/share/festival/voices/us/cmu_us_slt_arctic_hts/hts", "hts/*")

    pisitools.dodoc("COPYING", "README")
