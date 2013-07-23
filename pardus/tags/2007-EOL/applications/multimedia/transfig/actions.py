#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.util import join_path

WorkDir='transfig.3.2.5_alpha7'

def setup():
    pisitools.dosed("fig2dev/Imakefile", "\/usr\/local\/lib\/", "/usr/lib/")
    
    shelltools.system('xmkmf')
    autotools.make('Makefiles')

def build():
    autotools.make()

def install():
    autotools.make('install DESTDIR=%s' % get.installDIR())
    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL*", "NEWS", "README*")
