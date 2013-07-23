#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-error-on-warning \
                         --disable-static \
                         --enable-posix \
                         --enable-networking \
                         --enable-regex \
                         --enable-elisp \
                         --enable-nls \
                         --with-threads \
                         --with-modules")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "FAQ", "HACKING", "NEWS", "README", "THANKS")
