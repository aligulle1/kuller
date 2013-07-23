#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="emacs-20061105"

def setup():
    autotools.configure("--with-x \
                         --with-xpm \
                         --with-toolkit-scroll-bars \
                         --with-jpeg \
                         --with-tiff \
                         --with-gif \
                         --with-png \
                         --with-x-toolkit=gtk")


def build():
    autotools.make("bootstrap")

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "BUGS", "README")
