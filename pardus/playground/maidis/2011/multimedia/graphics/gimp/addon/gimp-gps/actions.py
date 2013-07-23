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
    pisitools.insinto("/usr/share/gimp/2.0/brushes", "brushes/*")
    pisitools.insinto("/usr/share/gimp/2.0/gradients", "gradients/*.ggr")
    pisitools.insinto("/usr/share/gimp/2.0/palettes", "palettes/*.gpl")
    pisitools.insinto("/usr/share/gimp/2.0/patterns", "patterns/*.pat")
    pisitools.insinto("/usr/share/gimp/2.0/tool-options", "tool-options/*")
    #pisitools.insinto("/etc/gimp/2.0", "sessionrc")
    pisitools.insinto("/etc/gimp/2.0", "toolrc")

    shelltools.chmod("%s/usr/share/gimp/2.0/brushes/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/gimp/2.0/gradients/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/gimp/2.0/palettes/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/gimp/2.0/patterns/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/gimp/2.0/tool-options/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/etc/gimp/2.0/*" % get.installDIR(), 0644)
