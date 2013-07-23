#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--with-default-dict=/usr/share/cracklib/pw_dict")

def build():
    autotools.make("all")

def install():
    autotools.install()

    # Create dictionary files
    shelltools.system("cat /usr/share/dict/words|%s/usr/sbin/cracklib-packer %s/usr/share/cracklib/pw_dict" % (get.installDIR(),get.installDIR()))

    pisitools.dodoc("HISTORY", "MANIFEST", "POSTER", "README")
    
    pisitools.domo("tr.po","tr","cracklib.mo")
