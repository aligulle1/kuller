#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

SCONS_ARCH = "x64" if get.ARCH() == "x86_64" else "ia32"

def build():
    scons.make("mode=release library=shared arch=%s" % SCONS_ARCH)
    scons.make("d8 arch=%s" % SCONS_ARCH)

def install():
    pisitools.dobin("d8")

    pisitools.dolib_so("libv8preparser.so")
    pisitools.dolib_so("libv8.so")

    pisitools.insinto("/usr/include", "include/*")

    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE*")
