#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir='xfig.3.2.5-alpha5'

def setup():
    pisitools.dosed("Imakefile", "\/usr\/local\/", "/usr/")
    shelltools.system('xmkmf')

def build():
    autotools.make("BINDIR=/usr/bin XFIGLIBDIR=/usr/lib/xfig")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    autotools.make('DESTDIR=%s \
                    BINDIR=/usr/bin \
                    XFIGLIBDIR=/usr/lib/xfig \
                    MANDIR=/usr/share/man/man1 \
                    MANSUFFIX=1 \
                    install.all' % get.installDIR())

    pisitools.dodoc("Doc/xfig_man.html", "Doc/xfig_ref_en.pdf")
    pisitools.dohtml("Doc/html/*")

    # conflicts with xorg
    pisitools.remove("/usr/lib/X11/app-defaults")
