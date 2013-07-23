#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.autoreconf()

    autotools.configure("--with-forced-embedded-ffmpeg")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("NEWS", "TODO", "README", "AUTHORS", "ChangeLog")
