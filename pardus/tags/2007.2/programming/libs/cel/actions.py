#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "cel"

def setup():
    autotools.configure("--disable-optimize-mode-debug-info \
                         --disable-jamtest \
                         --with-cs-prefix=/usr \
                         --with-python \
                         --enable-cpu-specific-optimizations=no \
                         --disable-separate-debug-info \
                         --disable-debug \
                         --without-bfd")

def build():
    pisitools.dosed("Jamconfig", "-O3", get.CFLAGS())
    pisitools.dosed("Jamconfig", "/usr/local/lib", "/usr/lib")

    shelltools.system("jam")

def install():
    for f in ("install_bin", "install_plugin", "install_lib",
              "install_include", "install_data", "install_config", "install_doc"):
        shelltools.system("jam -s DESTDIR=%s %s" % (get.installDIR(), f))

    pisitools.domove("/%s/cel/*" % get.docDIR(), "/%s/%s" % (get.docDIR(), get.srcTAG()))
    pisitools.removeDir("/%s/cel" % get.docDIR())
    pisitools.dodoc("COPYING", "README")
