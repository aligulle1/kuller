#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "recipe-0.1~2~16~201105270934"

def install():
    pisitools.dobin("src/emgd-xorg-conf.py")
    pisitools.rename("/usr/bin/emgd-xorg-conf.py", "emgd-xorg-conf") 

    pisitools.dodoc("debian/changelog", "debian/copyright")
