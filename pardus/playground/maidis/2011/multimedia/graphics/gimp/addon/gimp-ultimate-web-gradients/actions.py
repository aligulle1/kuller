#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    #üst geliştiricisine telif dosyasını arşive eklenmesi söylenecek
    pisitools.insinto("/usr/share/gimp/2.0/gradients", "gradients/*.ggr")

    pisitools.dodoc("README.txt")

    shelltools.chmod("%s/usr/share/gimp/2.0/gradients/*" % get.installDIR(), 0644)
