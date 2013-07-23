#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # To use the binaries from giflib
    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/usr/include")
    
    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "ONEWS", "UNCOMPRESSED_GIF", "README", "TODO", "doc/*.txt")
    pisitools.dohtml("doc/")
