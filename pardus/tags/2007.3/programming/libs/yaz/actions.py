#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dodoc("README","LICENSE","NEWS","Changelog","TODO")
    autotools.rawInstall("DESTDIR='%s' docdir='/%s/%s'" % (get.installDIR(), get.docDIR(), get.srcTAG()))
    pisitools.domove("/usr/share/doc/yaz/common/id.png", "/%s/%s" % (get.docDIR(), get.srcTAG()))
    pisitools.domove("/usr/share/doc/yaz/common/style1.css", "/%s/%s" % (get.docDIR(), get.srcTAG()))
    pisitools.removeDir("/usr/share/doc/yaz")
