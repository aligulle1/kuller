#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "fxload-2002_04_11"

def build():
    autotools.make("RPM_OPT_FLAGS=\"%s\"" % get.CFLAGS())

def install():
    autotools.rawInstall("prefix=%s" % get.installDIR())
