#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    autotools.configure("--with-audio=alsa \
                         --with-cpu=x86 \
                         --with-optimization=2 \
                         ")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.doman("mpg123.1")
    pisitools.dodoc("NEWS", "README", "AUTHORS", "doc/*")

