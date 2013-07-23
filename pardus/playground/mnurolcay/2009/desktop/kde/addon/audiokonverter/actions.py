#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="audiokonverter-%s" % get.srcVERSION()

def install():
    for binary in("anytowav4", "audioconvert4", "movie2sound4", "oggdrop-lx"):
        pisitools.dobin("%s" % binary, "/usr/kde/4/bin")

    pisitools.insinto("/usr/kde/4/share/kde4/services/ServiceMenus/", "*4.desktop")
    pisitools.insinto("/usr/kde/4/share/mimelnk/audio", "x-*.desktop")

    pisitools.dodoc("Changelog", "COPYING", "README", "TODO")
