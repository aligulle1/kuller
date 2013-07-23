#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "squidclamav"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dobin("squidclamav")
    pisitools.insinto("/etc", "squidclamav.conf.dist", "squidclamav.conf")
    pisitools.dodoc("ChangeLog", "README", "clwarn.cgi*")
