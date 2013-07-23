# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "psb-firmware"

def install():
    pisitools.insinto("/lib/firmware", "*.bin")
    pisitools.dodoc("COPYING")
