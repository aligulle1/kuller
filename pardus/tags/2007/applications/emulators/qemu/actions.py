#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

NoStrip="/usr/share/qemu"

def setup():
    autotools.rawConfigure('--prefix=/usr \
                            --enable-slirp \
                            --enable-alsa')
def build():
    autotools.make()

def install():
    install_dir = get.installDIR()
    autotools.make("install prefix=%s/usr bindir=%s/usr/bin datadir=%s/usr/share/qemu docdir=%s/usr/share/doc/qemu-%s-%s mandir=%s/usr/share/man"
                    % (install_dir,install_dir,install_dir,install_dir,get.srcVERSION(),get.srcRELEASE(),install_dir))
                    
    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL*", "NEWS", "README*")
