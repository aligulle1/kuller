#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    options = " --prefix=/usr \
                --openssldir=/etc/ssl \
                zlib enable-camellia enable-seed enable-tlsext enable-rfc3779 \
                threads shared -Wa,--noexecstack"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 --libdir=lib32"
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.system("./Configure linux-elf %s" % options)
    else:
        shelltools.system("./config %s" % options)
        pisitools.dosed("Makefile", "^(SHARED_LDFLAGS=).*", "\\1 ${LDFLAGS}")
        pisitools.dosed("Makefile", "^(CFLAG=.*)", "\\1 ${CFLAGS}")

def build():
    # triples compile time, be sure really needed.
    autotools.make("depend")
    autotools.make("-j1")
    autotools.make("rehash")

def install():
    if get.buildTYPE() != "emul32":
        pisitools.dolib_so("libcrypto.so.0.9.8")
        pisitools.dolib_so("libssl.so.0.9.8")

    if get.buildTYPE() == "emul32":
        pisitools.dolib_so("libcrypto.so.0.9.8", "/usr/lib32")
        pisitools.dolib_so("libssl.so.0.9.8", "/usr/lib32")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("ACKNOWLEDGMENTS", "CHANGES*", "FAQ", "LICENSE", "NEWS", "README", "doc/*.txt")
