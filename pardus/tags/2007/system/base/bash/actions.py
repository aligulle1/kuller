#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--without-installed-readline \
                         --disable-profiling \
                         --without-gnu-malloc \
                         --with-ncurses")

def build():
    autotools.make()

def install():
    autotools.install()
    
    pisitools.domove("/usr/bin/bash", "/bin")
    pisitools.dosym("/bin/bash","/bin/sh")
    pisitools.dosym("/bin/bash","/bin/rbash")
    
    pisitools.dodoc("README", "NEWS", "AUTHORS", "CHANGES", "COMPAT", "Y2K", "doc/FAQ", "doc/INTRO")
    pisitools.doman("doc/bash.1", "doc/bashbug.1", "doc/builtins.1", "doc/rbash.1")
    pisitools.dosym("bash.info", "/usr/share/info/bashref.info")
