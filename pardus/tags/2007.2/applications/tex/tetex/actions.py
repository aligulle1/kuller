# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="tetex-src-3.0"

def setup():
    install_dir = get.installDIR()
    pisitools.dodir("/usr/share/texmf")
    shelltools.sym("/usr/share/texmf-dist", "%s/usr/share/texmf-dist" % install_dir)
    autotools.rawConfigure("--prefix=%s/usr \
                            --bindir=%s/usr/bin \
                            --datadir=%s/usr/share \
                            --disable-multiplatform \
                            --with-xdvi-x-toolkit=xaw3d \
                            --with-system-ncurses \
                            --with-system-pnglib \
                            --with-system-zlib \
                            --with-system-gd \
                            --without-texinfo \
                            --without-dialog \
                            --without-texi2html \
                            --with-ps=gs \
                            --enable-ipc \
                            --with-etex \
                            --with-x" % (install_dir,install_dir,install_dir))

def build():
    autotools.make("-j1 world")

def install():
    pisitools.dodir("/var/cache/fonts")
    autotools.install()

    pisitools.dosed("%s/usr/share/texmf/web2c/texmf.cnf" % get.installDIR(), get.installDIR(), '')
    pisitools.dosed("%s/usr/share/texmf/web2c/texmf.cnf" % get.installDIR(), 'VARTEXFONTS = /var/tmp/texfonts', 'VARTEXFONTS  = /var/cache/fonts')

    pisitools.remove("/usr/share/texmf/ls-R")

