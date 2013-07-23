#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # dont compile samples
    pisitools.dosed("Makefile.in", "sample")

    autotools.configure("--enable-art \
                        --enable-rsvg \
                        --enable-glade \
                        --disable-gnome \
                        --disable-gnomevfs \
                        --disable-gtkhtml \
                        --disable-vte")

def build():
    # u really suck
    shelltools.export("LC_ALL", "C")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "README*")
