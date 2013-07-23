#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir="."

def setup():
    autotools.rawConfigure("--prefix-dir=/usr \
                            --binary-dir=/bin")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_DIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING","readme.txt","changelog.txt","known-bugs.txt")
