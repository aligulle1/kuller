#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # filter flag "-g3"
    # http://bugs.gentoo.org/26484
    shelltools.export("CFLAGS", get.CFLAGS().replace("-g3", "")) 
    autotools.configure()

def build():
    autotools.make()
    
def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "BUGS", "HACKING", "README")
