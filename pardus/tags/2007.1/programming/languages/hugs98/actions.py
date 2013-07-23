#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "hugs98-Mar2005-patched"

def setup():
    shelltools.export("hugsdir", "/usr/lib/hugs")
    autotools.configure("--enable-ffi \
                         --enable-profiling \
                         --enable-char-encoding=utf8 \
                         --enable-opengl \
                         --with-pthreads")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s prefix=/usr mandir=/usr/share/man" % get.installDIR())
    
    pisitools.domove("/usr/lib/hugs/docs/*", "/usr/share/doc/%s/" % get.srcTAG())
    pisitools.removeDir("/usr/lib/hugs/docs")
    pisitools.domove("/usr/lib/hugs/demos", "/usr/share/doc/%s/" % get.srcTAG())
    pisitools.remove("/usr/lib/hugs/Credits")
    pisitools.remove("/usr/lib/hugs/License")
    pisitools.remove("/usr/lib/hugs/Readme")
    pisitools.dodoc("Credits", "License", "Readme")
