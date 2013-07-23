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
    pisitools.dosed("configure", "-mno-ieee-fp")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("libvorbisfile.so.3.1.1", "/usr/lib/libvorbisfile.so.0")
    pisitools.dosym("libvorbisenc.so.2.0.2", "/usr/lib/libvorbisenc.so.0")

    pisitools.removeDir("/usr/share/doc")
    pisitools.dodoc("AUTHORS", "README", "todo.txt", "doc/*.txt")
    pisitools.dohtml("doc")
