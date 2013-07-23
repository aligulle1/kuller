# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/Makefile", "\/usr\/local\/include\/boost-1_35", "/usr/include/boost")

def build():
    autotools.make("CC=%s CXX=%s OPTFLAGS='%s' -C src" % (get.CC(), get.CXX(), get.CFLAGS()))

def install():
    pisitools.dobin("echoprint-codegen")
    pisitools.dolib_so("src/libcodegen.so")
    pisitools.insinto("/usr/include/echoprint", "src/Codegen.h")

    pisitools.dodoc("LICENSE", "README.md")
