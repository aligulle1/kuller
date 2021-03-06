#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure("--with-kde \
                   --with-vorbis \
                   --with-flac")

def build():
    kde.make()

def install():
    kde.install()
    pisitools.domo("po/tr.po","tr","kid3.mo")
