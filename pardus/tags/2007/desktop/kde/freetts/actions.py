#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.chmod("lib/jsapi.sh")

def build():
    shelltools.cd("lib/")
    shelltools.system("./jsapi.sh")
    shelltools.cd("../")
    shelltools.system("ant")
    
def install():
    pisitools.insinto("/usr/share/freetts/lib", "lib/*.jar")
    pisitools.insinto("/usr/share/freetts/lib", "mbrola/*.jar")

    pisitools.insinto("/usr/share/freetts", "speech.properties")
    
    pisitools.insinto("/usr/share/freetts", "demo/")
    pisitools.insinto("/usr/share/freetts", "tools/")

    pisitools.dodoc("README.txt", "RELEASE_NOTES", "acknowledgments.txt")


