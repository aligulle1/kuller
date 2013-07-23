#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "acpica-unix-%s" % get.srcVERSION().split('_')[-1]

def build():
    autotools.make("-C tools/acpisrc")
    autotools.make("-C tools/acpixtract")
    autotools.make("-C tools/acpiexec")

    autotools.make("-C compiler/ clean")
    autotools.make("-C compiler/")

def install():
    pisitools.dobin("compiler/iasl")
    pisitools.dosbin("tools/acpisrc/acpisrc")
    pisitools.dosbin("tools/acpiexec/acpiexec")
    pisitools.dosbin("tools/acpixtract/acpixtract")
